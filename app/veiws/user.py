import time
import random


from flask import Blueprint
from flask import request, jsonify, make_response

from app.model import tb_user
from app.utils.email import smtp


bp_user = Blueprint('user', __name__, url_prefix='/user')

# 用户TOKEN存储
user_token = {}
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
        print(verify_code)
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
        pass

    if request.method == "POST":
        pass


@bp_user.route("/info", methods=["GET"])
def user_info():
    if request.method == "GET":
        pass


@bp_user.route("/info/<path:subpath>", methods=["GET"])
def user_info_change(subpath):
    
    if request.method != "PUT":
        return jsonify(), 400

    if  subpath == "nickname":
        pass
    
    if  subpath == "portrait":
        pass

    if  subpath == "gender":
        pass


@bp_user.route("/address", methods=["GET", "POST", "PUT"])
def user_address():
    if request.method == "GET":
        pass

    if request.method == "POST":
        pass

    if request.method == "PUT":
        pass