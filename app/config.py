import random


class Config(object):
    DEBUG = True
    SECRET_KEY = "".join(str(i) for i in [random.randrange(0, 9) for _ in range(24)])

    # https://www.jianshu.com/p/f7ba338016b8/
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@192.168.0.195/db_example_store?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
