import os

from flask import Flask

from extensions import ma, db, migrate
from views import user_api


DEFAULT_BLUEPRINTS = (user_api,)


def create_app():
    app = Flask(__name__)

    for blueprint in DEFAULT_BLUEPRINTS:
        app.register_blueprint(blueprint)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    return app
