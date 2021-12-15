import os
import random


from flask import Blueprint
from flask import request, jsonify, session

from app.model import tb_user
from app.utils.email import smtp


bp_user = Blueprint('user', __name__, url_prefix='/user')


@bp_user.before_request
def authorization(*args, **kwargs):
    # print(request.path)
    if request.path == '/user/register/verify':
        return None
    if request.path == '/user/login/verify':
        return None

    tk = request.cookies.get("tk")
    if not tk:
        return jsonify(), 403

    if tk not in user_token:
        return jsonify(), 403

    user_id = user_token[tk]
    info = tb_user.get_user_info(user_id, None)
    if info:
        session["user_info"] = info
    else:
        return jsonify(), 403


# 用户TOKEN存储
user_token = {
    "16": 16
}

# 用户注册验证码存储
register_verify_code_store = {}
# 用户登陆验证码存储
login_verify_code_store = {}


@bp_user.route("/register/verify", methods=["GET", "POST"])
def user_register_verify():

    if request.method == "GET":
        email = str(request.args.get("email"))
        if not email:
            return jsonify(), 400

        if tb_user.email_existed(email):
            return jsonify(), 400

        verify_code = str(random.randint(1000, 9999))

        subject = "Example Store"
        content = "Register Verify Code: " + verify_code
        smtp.send(email, subject, content)

        register_verify_code_store[email] = verify_code
        return jsonify()

    if request.method == "POST":
        email = str(request.form.get("email"))
        verify_code = str(request.form.get("verify_code"))
        if not email or not verify_code:
            return jsonify(), 400

        if email not in register_verify_code_store:
            return jsonify(), 400

        if register_verify_code_store[email] == verify_code:
            register_verify_code_store.pop(email)
            tb_user.create_user(email)
            user_info = tb_user.get_user_info(None, email)
            tk = "".join(str(i) for i in [random.randrange(0, 9) for _ in range(12)])
            user_token[tk] = user_info["id"]

            resp = jsonify(user_info)
            resp.set_cookie(key="tk", value=tk)
            return resp, 200

        return jsonify(), 400


@bp_user.route("/login/verify", methods=["GET", "POST"])
def user_login_verify():
    if request.method == "GET":
        email = str(request.args.get("email"))
        if not email:
            return jsonify(), 400

        if not tb_user.email_existed(email):
            return jsonify(), 400

        verify_code = str(random.randint(1000, 9999))
        subject = "Example Store"
        content = "Login Verify Code: " + verify_code
        smtp.send(email, subject, content)

        login_verify_code_store[email] = verify_code
        return jsonify()

    if request.method == "POST":
        email = str(request.form.get("email"))
        verify_code = str(request.form.get("verify_code"))
        if not email or not verify_code:
            return jsonify(), 400

        if email not in login_verify_code_store:
            return jsonify(), 400

        if login_verify_code_store[email] == verify_code:
            login_verify_code_store.pop(email)

            user_info = tb_user.get_user_info(None, email)
            tk = "".join(str(i) for i in [random.randrange(0, 9) for _ in range(12)])
            for k in user_token:
                if user_token[k] == user_info["id"]:
                    del user_info[k]

            user_token[tk] = user_info["id"]
            resp = jsonify(user_info)
            resp.set_cookie(key="tk", value=tk)
            return resp, 200

        return jsonify(), 400


@bp_user.route("/info", methods=["GET"])
def user_info():
    if request.method == "GET":
        info = session.get("user_info")
        return jsonify(info), 200


@bp_user.route("/info/<path:subpath>", methods=["PUT"])
def user_info_change(subpath):

    info = session.get("user_info")

    if subpath == "nickname":
        new_nickname = request.form.get("new_nickname")
        if new_nickname == info["nickname"]:
            return jsonify(), 400
        tb_user.update_user_nickname(info["id"], new_nickname)
        new_info = tb_user.get_user_info(info["id"], None)
        session["user_info"] = new_info
        return jsonify(new_info), 200
    
    if subpath == "portrait":
        portrait_file = request.files.get("new_portrait")
        if not portrait_file:
            return jsonify(), 400

        dst = os.path.join("static", portrait_file.filename)
        portrait_file.save(dst)

        tb_user.update_user_portrait(info["id"], f"/{dst}")
        new_info = tb_user.get_user_info(info["id"], None)
        session["user_info"] = new_info
        return jsonify(new_info), 200

    if subpath == "gender":
        new_gender = request.form.get("new_gender", None)

        tb_user.update_user_gender(info["id"], new_gender)
        new_info = tb_user.get_user_info(info["id"], None)
        session["user_info"] = new_info
        return jsonify(new_info), 200


@bp_user.route("/address", methods=["GET", "POST", "PUT"])
def user_address():
    if request.method == "GET":
        pass

    if request.method == "POST":
        pass

    if request.method == "PUT":
        pass