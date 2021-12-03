import time
import random


from flask import Blueprint
from flask import request, jsonify

from app.model import tb_user
from app.utils.email import smtp


bp_user = Blueprint('user', __name__, url_prefix='/user')

register_verify_code_store = {}


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
            return jsonify(user_info), 200

        return jsonify(), 400
