from flask import Flask

import views
from database import Database
from ships import Ships
import os

import sqlite3 as dbapi2

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)   
    app.add_url_rule("/ships", view_func=views.ships_page) 
    app.add_url_rule("/alter_ship/<ship_id>", view_func=views.alter_ship)
    app.add_url_rule("/un_alter_ship/<ship_id>", view_func=views.un_alter_ship)
    app.add_url_rule("/delete_ship/<ship_id>", view_func=views.delete_ship)


    if(os.path.exists('./spacexhibit-data.db') ==False):

        con = dbapi2.connect("spacexhibit-data.db")
        print("Database is created and opened successfully")

        con.execute(
            "CREATE TABLE SHIPS ( SHIP_ID VARCHAR(80) PRIMARY KEY,NAME VARCHAR(80),TYPE VARCHAR(80),ACTIVE VARCHAR(80))")

        print("Movie table is created successfully")

        con.close()

    home_dir = os.getcwd()

    db = Database(os.path.join(home_dir, "spacexhibit-data.db"))

    # db = Database()  # Database object is created.

    #db.add_ship(Ship("Slaughterhouse-Five", "year=1972","3"))
    #db.add_ship(Ship("The Shining", "year=1972","3")) 

    app.config["dbconfig"] = db  

    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)