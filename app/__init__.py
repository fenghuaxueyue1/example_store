def create_app(config):

    from flask import Flask
    app = Flask(__name__)
    app.config.from_object(config)

    from app.model.model import db
    db.init_app(app)

    return app
