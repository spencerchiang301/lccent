import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-this-in-production'
    
    # MySQL 資料庫設定
    MYSQL_HOST = os.environ.get('MYSQL_HOST', '172.16.1.112')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'spencer')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'nicole')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'shopping_cart_db')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
    
    # Session 設定
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
    # 檔案上傳設定
    UPLOAD_FOLDER = 'static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB