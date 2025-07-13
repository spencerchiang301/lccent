import mysql.connector
from mysql.connector import Error
from contextlib import contextmanager
from config import Config

@contextmanager
def get_db_connection():
    """取得資料庫連接的 context manager"""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB,
            port=Config.MYSQL_PORT,
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci'
        )
        yield connection
    except Error as e:
        print(f"資料庫連接錯誤: {e}")
        raise
    finally:
        if connection and connection.is_connected():
            connection.close()

def execute_query(query, params=None, fetch_one=False, fetch_all=False):
    """執行 SQL 查詢"""
    with get_db_connection() as connection:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            
            if fetch_one:
                return cursor.fetchone()
            elif fetch_all:
                return cursor.fetchall()
            else:
                connection.commit()
                return cursor.lastrowid
        except Error as e:
            connection.rollback()
            print(f"查詢執行錯誤: {e}")
            raise
        finally:
            cursor.close()

def init_db():
    """初始化資料庫（僅供開發測試用）"""
    try:
        # 先連接到 MySQL 伺服器（不指定資料庫）
        connection = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            port=Config.MYSQL_PORT
        )
        cursor = connection.cursor()
        
        # 讀取並執行 schema.sql
        with open('schema.sql', 'r', encoding='utf-8') as f:
            sql_commands = f.read()
            
        # 分割 SQL 命令並逐一執行
        for command in sql_commands.split(';'):
            if command.strip():
                cursor.execute(command)
        
        connection.commit()
        print("資料庫初始化成功！")
        
    except Error as e:
        print(f"資料庫初始化錯誤: {e}")
        raise
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()