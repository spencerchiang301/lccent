from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os

from config import Config
from database import execute_query, init_db

app = Flask(__name__)
app.config.from_object(Config)
Session(app)

# 確保上傳目錄存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def login_required(f):
    """裝飾器：檢查使用者是否已登入"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('請先登入', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    """首頁"""
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """註冊頁面"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # 檢查使用者名稱是否已存在
        user = execute_query(
            "SELECT id FROM users WHERE username = %s OR email = %s",
            (username, email),
            fetch_one=True
        )
        
        if user:
            flash('使用者名稱或電子郵件已被使用', 'danger')
            return redirect(url_for('register'))
        
        # 建立新使用者
        password_hash = generate_password_hash(password)
        execute_query(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, password_hash)
        )
        
        flash('註冊成功！請登入', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """登入頁面"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # 查詢使用者
        user = execute_query(
            "SELECT id, username, password_hash FROM users WHERE username = %s OR email = %s",
            (username, username),
            fetch_one=True
        )
        
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('登入成功！', 'success')
            return redirect(url_for('products'))
        else:
            flash('使用者名稱或密碼錯誤', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """登出"""
    session.clear()
    flash('您已成功登出', 'info')
    return redirect(url_for('index'))

@app.route('/products')
def products():
    """產品列表頁面"""
    products = execute_query("SELECT * FROM products WHERE stock > 0", fetch_all=True)
    return render_template('products.html', products=products)

@app.route('/cart')
@login_required
def cart():
    """購物車頁面"""
    user_id = session['user_id']
    
    # 查詢購物車項目
    cart_items = execute_query(
        """
        SELECT c.id, c.quantity, p.id as product_id, p.name, p.price, p.image_url,
               (c.quantity * p.price) as subtotal
        FROM cart_items c
        JOIN products p ON c.product_id = p.id
        WHERE c.user_id = %s
        """,
        (user_id,),
        fetch_all=True
    )
    
    # 計算總金額
    total = sum(item['subtotal'] for item in cart_items)
    
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    """加入購物車"""
    user_id = session['user_id']
    quantity = int(request.form.get('quantity', 1))
    
    # 檢查產品是否存在
    product = execute_query(
        "SELECT id, stock FROM products WHERE id = %s",
        (product_id,),
        fetch_one=True
    )
    
    if not product:
        flash('產品不存在', 'danger')
        return redirect(url_for('products'))
    
    if product['stock'] < quantity:
        flash('庫存不足', 'warning')
        return redirect(url_for('products'))
    
    # 檢查購物車中是否已有此產品
    existing_item = execute_query(
        "SELECT id, quantity FROM cart_items WHERE user_id = %s AND product_id = %s",
        (user_id, product_id),
        fetch_one=True
    )
    
    if existing_item:
        # 更新數量
        new_quantity = existing_item['quantity'] + quantity
        execute_query(
            "UPDATE cart_items SET quantity = %s WHERE id = %s",
            (new_quantity, existing_item['id'])
        )
    else:
        # 新增項目
        execute_query(
            "INSERT INTO cart_items (user_id, product_id, quantity) VALUES (%s, %s, %s)",
            (user_id, product_id, quantity)
        )
    
    flash('已加入購物車', 'success')
    return redirect(url_for('products'))

@app.route('/cart/update/<int:item_id>', methods=['POST'])
@login_required
def update_cart_item(item_id):
    """更新購物車項目數量"""
    user_id = session['user_id']
    quantity = int(request.form.get('quantity', 1))
    
    if quantity <= 0:
        execute_query(
            "DELETE FROM cart_items WHERE id = %s AND user_id = %s",
            (item_id, user_id)
        )
        flash('已從購物車移除', 'info')
    else:
        execute_query(
            "UPDATE cart_items SET quantity = %s WHERE id = %s AND user_id = %s",
            (quantity, item_id, user_id)
        )
        flash('購物車已更新', 'success')
    
    return redirect(url_for('cart'))

@app.route('/cart/remove/<int:item_id>')
@login_required
def remove_from_cart(item_id):
    """從購物車移除項目"""
    user_id = session['user_id']
    
    execute_query(
        "DELETE FROM cart_items WHERE id = %s AND user_id = %s",
        (item_id, user_id)
    )
    
    flash('已從購物車移除', 'info')
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['POST'])
@login_required
def checkout():
    """結帳"""
    user_id = session['user_id']
    
    # 查詢購物車項目
    cart_items = execute_query(
        """
        SELECT c.quantity, p.id as product_id, p.price, p.stock
        FROM cart_items c
        JOIN products p ON c.product_id = p.id
        WHERE c.user_id = %s
        """,
        (user_id,),
        fetch_all=True
    )
    
    if not cart_items:
        flash('購物車是空的', 'warning')
        return redirect(url_for('cart'))
    
    # 檢查庫存
    for item in cart_items:
        if item['stock'] < item['quantity']:
            flash('部分商品庫存不足', 'danger')
            return redirect(url_for('cart'))
    
    # 計算總金額
    total_amount = sum(item['quantity'] * item['price'] for item in cart_items)
    
    # 建立訂單
    order_id = execute_query(
        "INSERT INTO orders (user_id, total_amount) VALUES (%s, %s)",
        (user_id, total_amount)
    )
    
    # 建立訂單明細並更新庫存
    for item in cart_items:
        # 建立訂單明細
        execute_query(
            "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)",
            (order_id, item['product_id'], item['quantity'], item['price'])
        )
        
        # 更新產品庫存
        execute_query(
            "UPDATE products SET stock = stock - %s WHERE id = %s",
            (item['quantity'], item['product_id'])
        )
    
    # 清空購物車
    execute_query("DELETE FROM cart_items WHERE user_id = %s", (user_id,))
    
    flash('訂單已成功建立！', 'success')
    return redirect(url_for('orders'))

@app.route('/orders')
@login_required
def orders():
    """訂單列表頁面"""
    user_id = session['user_id']
    
    # 查詢使用者的訂單
    orders = execute_query(
        """
        SELECT id, total_amount, status, created_at
        FROM orders
        WHERE user_id = %s
        ORDER BY created_at DESC
        """,
        (user_id,),
        fetch_all=True
    )
    
    # 查詢每個訂單的明細
    for order in orders:
        order['items'] = execute_query(
            """
            SELECT oi.quantity, oi.price, p.name
            FROM order_items oi
            JOIN products p ON oi.product_id = p.id
            WHERE oi.order_id = %s
            """,
            (order['id'],),
            fetch_all=True
        )
    
    return render_template('orders.html', orders=orders)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # 開發環境下初始化資料庫
    if os.environ.get('FLASK_ENV') == 'development':
        try:
            init_db()
        except Exception as e:
            print(f"資料庫初始化失敗: {e}")
    
    app.run(host='0.0.0.0', port=5000, debug=True)