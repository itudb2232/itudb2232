from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'DummyKey'

    # import the blueprints from views.py
    from views import views

    # now we register the blueprints
    app.register_blueprint(views, url_prefix = '/')

    app.config["db"] = "spacexhibit-data.db"
    app.config["user-db"] = "user-data.db"

    return app