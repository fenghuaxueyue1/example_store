import random


class Config(object):
    DEBUG = True
    SECRET_KEY = "".join(str(i) for i in [random.randrange(0, 9) for _ in range(24)])

    # server
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 5000
    
    # db
    DB_USER = "root"
    DB_PSWD = "123456"
    DB_HOST = "192.168.0.197"
    DB_PORT = 3306
    DB_NAME = "db_example_store"

    # smtp
    SMTP_USER = "example_inform@163.com"
    SMTP_PSWD = "DCLGXQCVDOHSNXWV"
    SMTP_HOST = "smtp.163.com"
