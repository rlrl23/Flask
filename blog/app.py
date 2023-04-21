from flask import Flask
from .models.database import db
from .views.users import users_app
from .views.articles import articles_app
from .views.index import index
from .views.auth import login_manager, auth_app


VIEWS = [
    index,
    users_app,
    articles_app,
    auth_app,
]
def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY']="adcd12345678"
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)


