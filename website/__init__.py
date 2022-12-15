from flask import Flask
from flask_login import LoginManager

import views
from users import get_user


lm = LoginManager()

@lm.user_loader
def load_user(username):
    return get_user(username)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'DummyKey'

    # now we register the blueprints
    app.register_blueprint(views.views, url_prefix = '/')

    app.config["db"] = "spacexhibit-data.db"
    app.config["user-db"] = "user-data.db"

    app.add_url_rule("/login", view_func=views.login, methods=["GET", "POST"])
    app.add_url_rule("/logout", view_func=views.home)

    lm.init_app(app)
    lm.login_view = "views.login"

    return app