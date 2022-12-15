from flask import current_app
from flask_login import UserMixin

import sqlite3

class User(UserMixin):
    def __init__(self, username, password, type) -> None:
        self.username = username
        self.password = password
        self.active = True
        self.is_admin = True if type == "admin" else False
    
        def get_id(self):
            return self.username

        @property
        def is_active(self):
            return self.active
    
    def get_user(user_id):
        user_db = sqlite3.connect(current_app.config["user-db"]).cursor()
        user_db.row_factory = sqlite3.Row
        user_data = user_db.cursor().execute("SELECT * FROM users WHERE username = ?", user_id).fetchall()

        if len(user_data) == 1:
            return User(user_data[0]["username"], user_data[0]["password"])


def get_user(user_id):
    password = current_app.config["PASSWORDS"].get(user_id)
    user = User(user_id, password) if password else None
    if user is not None:
        user.is_admin = user.username in current_app.config["ADMIN_USERS"]
    return user
    