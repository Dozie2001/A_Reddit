from flask import Flask
from api.extensions import db, migrate
from api.config import AppConfig

def make_app():
    app = Flask(__name__)
    app.config.from_object(AppConfig)
    db.init_app(app)
    migrate.init_app(app)

    from api.controller.user_paths import user_router

    app.register_blueprint(user_router)
    return app
