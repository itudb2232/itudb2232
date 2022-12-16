import sqlite3
from flask import current_app

db_location = "spacexhibit-data.db"

def get_launches():
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        return cur.execute(
            "SELECT * FROM launches JOIN launch_details on launches.launch_id = launch_details.launch_id"
            ).fetchall()

def get_rockets():
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        return cur.execute(
            "SELECT * FROM rockets"
            ).fetchall()

def get_rocket_d1():
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        return cur.execute(
            "SELECT * FROM rocket_details_1"
            ).fetchall()

def get_cores():
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        return cur.execute(
            "SELECT * FROM cores"
            ).fetchall()

def get_capsules():
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        return cur.execute(
            "SELECT * FROM capsules"
            ).fetchall()

def get_ships(request):
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        if request.method == 'POST':
            query = "SELECT * FROM ships"
            params = []
            if request.form.get('name'):
                if not params:
                    query += " WHERE"
                user_name = request.form['name']
                query += " name LIKE ?"
                param_name = "%" + user_name + "%"
                params.append(param_name)

            if request.form.get('type'):
                if not params:
                    query += " WHERE"
                else:
                    query += " AND"
                user_type = request.form['type']
                query += " type LIKE ?"
                param_type = "%" + user_type + "%"
                params.append(param_type)

            if request.form.get('active'):
                user_active = request.form['active']
                if not params:
                    query += " WHERE"
                else:
                    query += " AND"
                query += " active LIKE ?"
                param_active = "%" + user_active + "%"
                print("paramactive: " + param_active)
                params.append(param_active)

            cur.execute(query, tuple(params))
            ships = cur.fetchall()
            cur.execute("SELECT * FROM ship_details_1 ORDER BY ship_id ASC")
            ship_details_1 = cur.fetchall()
        
        else:
            ships = cur.execute("SELECT * FROM ships ORDER BY ship_id ASC").fetchall()
            cur.execute("SELECT * FROM ship_details_1 ORDER BY ship_id ASC")
            ship_details_1 = cur.fetchall()

        return ships, ship_details_1

def get_ship_d2():
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        return cur.execute(
            "SELECT * FROM ship_details_2"
            ).fetchall()

def get_payloads():
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        return cur.execute(
            "SELECT * FROM payloads ORDER BY name ASC"
            ).fetchall()

def add_payload(request):
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor() 

        # Add new payload
        payload_columns = cur.execute("PRAGMA table_info(payloads)").fetchall()

        new_payload = [str(current_app.config["payload_id"])]  # Get next ID
        current_app.config["payload_id"] += 1
        for column in payload_columns:
            if column["name"] in request.form.keys():
                new_payload += [request.form[column["name"]]]

        cur.execute(f'INSERT INTO payloads VALUES ({",".join("?" * len(payload_columns))})', new_payload)
        con.commit()

def delete_launches(launch_id):
        with sqlite3.connect(db_location) as con:
            cursor = con.cursor()
            query = "DELETE FROM launches WHERE (launch_id = ?)"
            cursor.execute(query, (launch_id,))
            con.commit()
