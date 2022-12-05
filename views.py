from datetime import datetime

from flask import current_app, render_template
from ships import Ships


def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)


def ships_page():
    myDB = current_app.config["dbconfig"]
    ships = myDB.get_ships()
    print(ships)
    return render_template("ships.html", ships=sorted(ships))


def alter_ship(ship_id):
    myDB = current_app.config["dbconfig"]
    current_ship = myDB.get_ship(ship_id)
    new_ship_name = "Updated " + current_ship.name
    if current_ship.type != None:
        new_ship_type = current_ship.type + "100"
        new_ship_object = Ships(new_ship_name, new_ship_type)
    else:
        new_ship_object = Ships(new_ship_name)
    myDB.update_ship(ship_id, new_ship_object)
    ships = myDB.get_ships()

    return render_template("ships.html", ships=sorted(ships))


def un_alter_ship(ship_id):
    myDB = current_app.config["dbconfig"]
    current_ship = myDB.get_ship(ship_id)
    new_ship_name = current_ship.name.replace("Updated", "")
    if current_ship.type != None:
        new_ship_type = current_ship.type + "100"       #!!!!!!!!!!!!!!!!!!!!!
        new_ship_object = Ships(new_ship_name, new_ship_type)
    else:
        new_ship_object = Ships(new_ship_name)

    myDB.update_ship(ship_id, new_ship_object)
    ships = myDB.get_ships()

    return render_template("ships.html", ships=sorted(ships))


def delete_ship(ship_id):
    myDB = current_app.config["dbconfig"]
    myDB.delete_ship(ship_id)
    ships = myDB.get_ships()


    return render_template("ships.html", ships=sorted(ships))