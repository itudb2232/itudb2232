import sqlite3
from flask import current_app

db_location = "spacexhibit-data.db"

# Capsules
def get_capsules():
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        return cur.execute(
            "SELECT * FROM capsules"
            ).fetchall()

def add_capsule(request):
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor() 

        # Add new capsule
        capsule_columns = cur.execute("PRAGMA table_info(capsules)").fetchall()
        
        new_capsule = []
        for column in capsule_columns:
            if column["name"] in request.form.keys():
                new_capsule += [request.form[column["name"]]]

        cur.execute(f'INSERT INTO capsules VALUES ({",".join("?" * len(capsule_columns))})', new_capsule)
        con.commit()

def delete_capsule(capsule_id):
    with sqlite3.connect(db_location) as con:
        cursor = con.cursor()
        query = "DELETE FROM capsules WHERE (capsule_id = ?)"
        cursor.execute(query, (capsule_id,))
        con.commit()

# Cores
def get_cores():
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        return cur.execute(
            "SELECT * FROM cores"
            ).fetchall()

def add_core(request):
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor() 

        # Add new core
        core_columns = cur.execute("PRAGMA table_info(cores)").fetchall()

        new_core = [str(current_app.config["core_id"])]  # Get next ID
        current_app.config["core_id"] += 1
        for column in core_columns:
            if column["serial"] in request.form.keys():
                new_core += [request.form[column["serial"]]]

        cur.execute(f'INSERT INTO cores VALUES ({",".join("?" * len(core_columns))})', new_core)
        con.commit()
        
def delete_core(core_id):
    with sqlite3.connect(db_location) as con:
        cursor = con.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        query = "DELETE FROM cores WHERE (core_id = ?)"
        cursor.execute(query, (core_id,))
        con.commit()

def update_core(request):
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        core_columns = cur.execute("PRAGMA table_info(rockets)").fetchall()
        core_columns_str = ",".join([column["serial"] + "=?" for column in core_columns if column["serial"] != "core_id"])

        rocket = []
        for column in core_columns:
            if column["serial"] in request.form.keys():
                rocket += [request.form[column["serial"]]]
        
        core_id = core[0]
        core = core[1:] + [core_id]

        cur.execute(f'UPDATE cores SET {core_columns_str} WHERE core_id = ?', rocket)
        con.commit()

# Launches
def get_launches():
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        return cur.execute(
            "SELECT * FROM launches JOIN launch_details on launches.launch_id = launch_details.launch_id"
            ).fetchall()

def add_launch(request):
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor() 

        # Add new launch
        launch_columns = cur.execute("PRAGMA table_info(launches)").fetchall()
        
        new_launch = []
        for column in launch_columns:
            if column["name"] in request.form.keys():
                new_launch += [request.form[column["name"]]]

        cur.execute(f'INSERT INTO launches VALUES ({",".join("?" * len(launch_columns))})', new_launch)
        con.commit()

def delete_launch(launch_id):
        with sqlite3.connect(db_location) as con:
            cursor = con.cursor()
            query = "DELETE FROM launches WHERE (launch_id = ?)"
            cursor.execute(query, (launch_id,))
            con.commit()

# Launchpads
def get_launchpads():
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        return cur.execute(
            "SELECT * FROM launchpads ORDER BY name"
        )

# Payloads
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

# Rockets
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
            """SELECT * FROM rocket_details_1 
            JOIN (SELECT rocket_id, name FROM rockets) AS rocket_names
            ON rocket_details_1.rocket_id = rocket_names.rocket_id"""
            ).fetchall()
def get_rocket_d2():
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        return cur.execute(
            """SELECT * FROM rocket_details_2 
            JOIN (SELECT rocket_id, name FROM rockets) AS rocket_names
            ON rocket_details_2.rocket_id = rocket_names.rocket_id"""
            ).fetchall()
def get_rocket_image():
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        data = cur.execute(
            """SELECT * FROM rocket_images
            JOIN (SELECT rocket_id, name FROM rockets) AS rocket_names
            ON rocket_images.rocket_id = rocket_names.rocket_id"""
            ).fetchall()
        for row in data:
            try:
                with open("/static/rocket_images/" + row["rocket_id"] + ".png", "wb+") as image_file:
                    image_file.write(row["rocket_image"])
            except FileNotFoundError:
                with open("website/static/rocket_images/" + row["rocket_id"] + ".png", "wb+") as image_file:
                    image_file.write(row["rocket_image"])
        return data

def add_rocket(request):
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor() 

        # Add new rocket
        rocket_columns = cur.execute("PRAGMA table_info(rockets)").fetchall()

        new_rocket = [str(current_app.config["rocket_id"])]  # Get next ID
        current_app.config["rocket_id"] += 1
        for column in rocket_columns:
            if column["name"] in request.form.keys():
                new_rocket += [request.form[column["name"]]]

        cur.execute(f'INSERT INTO rockets VALUES ({",".join("?" * len(rocket_columns))})', new_rocket)
        con.commit()
def add_rocket_d1(request):
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor() 

        # Add new rocket_d1
        rocket_d1_columns = cur.execute("PRAGMA table_info(rocket_details_1)").fetchall()
        
        new_rocket_d1 = []
        for column in rocket_d1_columns:
            if column["name"] in request.form.keys():
                new_rocket_d1 += [request.form[column["name"]]]

        cur.execute(f'INSERT INTO rocket_details_1 VALUES ({",".join("?" * len(rocket_d1_columns))})', new_rocket_d1)
        con.commit()
def add_rocket_d2(request):
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor() 

        # Add new rocket_d2
        rocket_d2_columns = cur.execute("PRAGMA table_info(rocket_details_2)").fetchall()
        
        new_rocket_d2 = []
        for column in rocket_d2_columns:
            if column["name"] in request.form.keys():
                new_rocket_d2 += [request.form[column["name"]]]

        cur.execute(f'INSERT INTO rocket_details_2 VALUES ({",".join("?" * len(rocket_d2_columns))})', new_rocket_d2)
        con.commit()
def add_rocket_image(request):
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor() 

        # Add new rocket_image
        
        new_rocket_image = [request.form["rocket_id"]]

        data = request.files["rocket_image"].read()
        print(data)

        new_rocket_image += [data]

        cur.execute(f'INSERT INTO rocket_images VALUES (?, ?)', new_rocket_image)
        con.commit()

def update_rocket(request):
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        # Update rocket
        rocket_columns = cur.execute("PRAGMA table_info(rockets)").fetchall()
        rocket_columns_str = ",".join([column["name"] + "=?" for column in rocket_columns if column["name"] != "rocket_id"])

        rocket = []
        for column in rocket_columns:
            if column["name"] in request.form.keys():
                rocket += [request.form[column["name"]]]
        
        rocket_id = rocket[0]
        rocket = rocket[1:] + [rocket_id]

        cur.execute(f'UPDATE rockets SET {rocket_columns_str} WHERE rocket_id = ?', rocket)
        con.commit()
def update_rocket_d1(request):
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        # Update rocket_d1
        rocket_d1_columns = cur.execute("PRAGMA table_info(rocket_details_1)").fetchall()
        rocket_d1_columns_str = ",".join([column["name"] + "=?" for column in rocket_d1_columns if column["name"] != "rocket_id"])
        
        rocket_d1 = []
        for column in rocket_d1_columns:
            if column["name"] in request.form.keys():
                rocket_d1 += [request.form[column["name"]]]

        rocket_id = rocket_d1[0]
        rocket_d1 = rocket_d1[1:] + [rocket_id]

        cur.execute(f'UPDATE rocket_details_1 SET {rocket_d1_columns_str} WHERE rocket_id = ?', rocket_d1)
        con.commit()
def update_rocket_d2(request):
    with sqlite3.connect(db_location) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        # Update rocket_d2
        rocket_d2_columns = cur.execute("PRAGMA table_info(rocket_details_2)").fetchall()
        rocket_d2_columns_str = ",".join([column["name"] + "=?" for column in rocket_d2_columns if column["name"] != "rocket_id"])
        
        rocket_d2 = []
        for column in rocket_d2_columns:
            if column["name"] in request.form.keys():
                rocket_d2 += [request.form[column["name"]]]

        rocket_id = rocket_d2[0]
        rocket_d2 = rocket_d2[1:] + [rocket_id]

        cur.execute(f'UPDATE rocket_details_2 SET {rocket_d2_columns_str} WHERE rocket_id = ?', rocket_d2)
        con.commit()

def delete_rocket(rocket_id):
    with sqlite3.connect(db_location) as con:
        cursor = con.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")  # This allows for cascading to details
        query = "DELETE FROM rockets WHERE (rocket_id = ?)"
        cursor.execute(query, (rocket_id,))
        con.commit()
def delete_rocket_d1(rocket_id):
    with sqlite3.connect(db_location) as con:
        cursor = con.cursor()
        query = "DELETE FROM rocket_details_1 WHERE (rocket_id = ?)"
        cursor.execute(query, (rocket_id,))
        con.commit()
def delete_rocket_d2(rocket_id):
    with sqlite3.connect(db_location) as con:
        cursor = con.cursor()
        query = "DELETE FROM rocket_details_2 WHERE (rocket_id = ?)"
        cursor.execute(query, (rocket_id,))
        con.commit()
def delete_rocket_image(rocket_id):
    with sqlite3.connect(db_location) as con:
        cursor = con.cursor()
        query = "DELETE FROM rocket_images WHERE (rocket_id = ?)"
        cursor.execute(query, (rocket_id,))
        con.commit()

# Ships
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
