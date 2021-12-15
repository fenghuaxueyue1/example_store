import time

import pymysql

from . import db
from app.utils.gen_portrait import Avatar, GEOMETRIC


def email_existed(email: str) -> bool:
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = f"SELECT COUNT(*) AS 'count' FROM tb_user WHERE email = '{email}'"
    cursor.execute(sql)
    ret = cursor.fetchone()
    cursor.close()
    if ret["count"] == 1:
        return True

    return False


def create_user(email: str) -> bool:
    nickname = ""
    if len(email.split("@")[0]) >= 3:
        nickname = email.split("@")[0][0]
        nickname += "*" * len(email.split("@")[0][1:-1])
        nickname += email.split("@")[0][-1]
    elif len(email.split("@")[0]) == 2:
        nickname = email.split("@")[0][0] + "*"
    elif len(email.split("@")[0]) == 1:
        nickname = "*"
    nickname += "@" + email.split("@")[1]

    portrait = Avatar(GEOMETRIC, 128).generate(email)
    cursor = db.cursor()
    sql = f"INSERT INTO tb_user (nickname, portrait, email, create_timestamp) VALUES" \
          f" {nickname, portrait, email, time.time().__int__()}"
    cursor.execute(sql)
    db.commit()


def get_user_info(user_id: int, email: str) -> dict:
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = f"SELECT * FROM tb_user WHERE email = '{email}'"
    if user_id:
        sql = f"SELECT * FROM tb_user WHERE id = '{user_id}'"
    cursor.execute(sql)
    ret = cursor.fetchone()
    ret.pop("email")
    cursor.close()
    return ret


def update_user_nickname(user_id: int, new_nickname: str):
    cursor = db.cursor()
    sql = f"UPDATE tb_user SET nickname='{new_nickname}' WHERE id = '{user_id}'"
    cursor.execute(sql)
    db.commit()


def update_user_portrait(user_id: int, new_portrait: str):
    cursor = db.cursor()
    sql = f"UPDATE tb_user SET portrait='{new_portrait}' WHERE id = '{user_id}'"
    cursor.execute(sql)
    db.commit()


def update_user_gender(user_id: int, new_gender: int):
    cursor = db.cursor()
    sql = f"UPDATE tb_user SET gender='{new_gender}' WHERE id = '{user_id}'"
    cursor.execute(sql)
    db.commit()