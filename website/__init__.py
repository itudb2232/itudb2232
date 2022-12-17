from flask import Flask
from flask_login import LoginManager

import views
from users import get_user
import database

lm = LoginManager()

@lm.user_loader
def load_user(username):
    return get_user(username)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'DummyKey'

    # now we register the blueprints
    app.register_blueprint(views.views, url_prefix = '/')

    app.config["user-db"] = "user-data.db"

    lm.init_app(app)
    lm.login_view = "views.login"

    # Set latest IDs for insertable tables

    payload_id = -1
    for payload in database.get_payloads():
        current_id = payload["payload_id"]
        if current_id.isdigit():
            if int(current_id) > int(payload_id):
                payload_id = current_id
    app.config["payload_id"] = int(payload_id) + 1
    
    rocket_id = -1
    for rocket in database.get_rockets():
        current_id = rocket["rocket_id"]
        if current_id.isdigit():
            if int(current_id) > int(rocket_id):
                rocket_id = current_id
    app.config["rocket_id"] = int(rocket_id) + 1
    
    rocket_id = -1
    for rocket in database.get_rockets():
        current_id = rocket["rocket_id"]
        if current_id.isdigit():
            if int(current_id) > int(rocket_id):
                rocket_id = current_id
    app.config["rocket_id"] = int(rocket_id) + 1

    return app