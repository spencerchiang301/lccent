# Flask 購物車系統

這是一個使用 Flask 和 MySQL 建立的教學用購物車系統，使用純 SQL 語法而非 ORM。

## 功能特色

- 使用者認證系統（註冊、登入、登出）
- 商品瀏覽
- 購物車功能（新增、更新數量、刪除）
- 訂單管理
- 響應式網頁設計

## 系統需求

- Python 3.8+
- MySQL 5.7+
- pip

## 安裝步驟

1. 安裝相依套件：
```bash
pip install -r requirements.txt
```

2. 設定 MySQL 資料庫：
   - 確保 MySQL 服務正在執行
   - 修改 `config.py` 中的資料庫連接設定（使用者名稱、密碼等）

3. 初始化資料庫：
```bash
# 在 MySQL 中執行 schema.sql
mysql -u root -p < schema.sql

# 或者設定環境變數後執行應用程式（會自動初始化）
export FLASK_ENV=development
python app.py
```

## 設定說明

在 `config.py` 中可以修改以下設定：

- `SECRET_KEY`: Flask 應用程式密鑰（生產環境請更換）
- `MYSQL_HOST`: MySQL 主機位址
- `MYSQL_USER`: MySQL 使用者名稱
- `MYSQL_PASSWORD`: MySQL 密碼
- `MYSQL_DB`: 資料庫名稱
- `MYSQL_PORT`: MySQL 連接埠

## 執行應用程式

```bash
python app.py
```

應用程式會在 http://localhost:5000 啟動

## 專案結構

```
shopping_cart/
├── app.py              # 主應用程式
├── config.py           # 設定檔
├── database.py         # 資料庫連接模組
├── schema.sql          # 資料庫架構
├── requirements.txt    # Python 套件清單
├── templates/          # HTML 模板
│   ├── base.html      # 基礎模板
│   ├── index.html     # 首頁
│   ├── login.html     # 登入頁
│   ├── register.html  # 註冊頁
│   ├── products.html  # 商品列表
│   ├── cart.html      # 購物車
│   └── orders.html    # 訂單列表
└── static/            # 靜態檔案
    ├── css/
    │   └── style.css  # 自訂樣式
    └── js/
        └── main.js    # JavaScript 功能
```

## 注意事項

1. 這是教學範例專案，請勿直接用於生產環境
2. 生產環境需要：
   - 更換 SECRET_KEY
   - 使用環境變數管理敏感資訊
   - 加入更完整的錯誤處理
   - 實作 CSRF 保護
   - 使用 HTTPS
   - 加入更多安全措施

## 測試帳號

系統初始化後會建立測試商品，但沒有預設使用者帳號。請自行註冊新帳號進行測試。