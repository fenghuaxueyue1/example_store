import pymysql

from app.config import Config

db = pymysql.connect(
    user=Config.DB_USER, password=Config.DB_PSWD, host=Config.DB_HOST, port=Config.DB_PORT, database=Config.DB_NAME
)
