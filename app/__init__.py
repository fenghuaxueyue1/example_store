from flask import Flask


def create_app(config):

    app = Flask(__name__)
    app.config.from_object(config)

    from app.veiws.user import bp_user
    app.register_blueprint(bp_user)

    return app
