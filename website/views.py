# This file is for arranging which pages the user can navigate to (i.e. launchpads, launches, rockets, ships...) #
# This file is a blueprint, it has a bunch of roots and urls inside of it #

from flask import Blueprint, render_template, current_app, request, redirect, url_for
import sqlite3
from flask_login import current_user

from time import time_ns
from random import random

import forms

views = Blueprint('views', __name__)

# Userlogin page
@views.route('/login')
def login():
    return render_template("login.html", form=forms.LoginForm())

@views.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    # Check if username and password
    if valid_login(username, password):
        return redirect(url_for('views.home'))
    else:
        return redirect(url_for('views.login'))

@views.route('/home')
@views.route("/")
def home():
    return render_template("home.html")

def valid_login(username, password):
    if not username or not password:
        return False

    with open('users.txt') as f:
        lines = f.readlines()

    for line in lines:
        uname, pword = line.strip().split(':')
        if uname == username and pword == password:
            return True

    return False

@views.route('/launches', methods=['GET', 'POST'])
def launches():
    con = sqlite3.connect(current_app.config["db"])
    con.row_factory = sqlite3.Row
    cur = con.cursor() 
    launches = cur.execute("SELECT * FROM launches JOIN launch_details on launches.launch_id = launch_details.launch_id").fetchall()
    return render_template("launches.html", launches=launches)

@views.route('/launchpads', methods=['GET', 'POST'])
def launchpads():
    return render_template("launchpads.html")

@views.route('/rockets', methods=['GET', 'POST'])
def rockets():
    con = sqlite3.connect(current_app.config["db"])
    con.row_factory = sqlite3.Row  # Query returns objects
    cur = con.cursor() 
    rockets = cur.execute("SELECT * FROM rockets").fetchall()
    return render_template("rockets.html", rockets=rockets)

@views.route('/rockets/rocket_details_1', methods=['GET', 'POST'])
def rocket_details_1():
    con = sqlite3.connect(current_app.config["db"])
    con.row_factory = sqlite3.Row
    cur = con.cursor() 
    cores = cur.execute("SELECT * FROM rocket_details_1").fetchall()
    return render_template("rocket_details_1.html", rocket_details_1=rocket_details_1)



@views.route('/ships', methods=['GET', 'POST'])
def ships():
    con = sqlite3.connect(current_app.config["db"])
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

    return render_template("ships.html",ships=ships, ship_details_1=ship_details_1)



@views.route('/ships/ship_details_2', methods=['GET', 'POST'])
def ship_details_2():
    con = sqlite3.connect(current_app.config["db"])
    con.row_factory = sqlite3.Row  
    cur = con.cursor() 
    ship_details_2 = cur.execute("SELECT * FROM ship_details_2").fetchall()
    return render_template("ship_details_2.html",ship_details_2=ship_details_2)

@views.route('/payloads', methods=['GET', 'POST'])
def payloads():
    if request.method == "GET":
        con = sqlite3.connect(current_app.config["db"])
        con.row_factory = sqlite3.Row  # Query returns objects
        cur = con.cursor() 
        payloads = cur.execute("SELECT * FROM payloads ORDER BY name ASC").fetchall()
        insert_data = request.form
        print(insert_data)
        return render_template("payloads.html", payloads=payloads)
    else:
        con = sqlite3.connect(current_app.config["db"])
        con.row_factory = sqlite3.Row  # Query returns objects
        cur = con.cursor() 

        # Add new payload
        n = request.form
        new_tuple = (str(time_ns()) + str(random())[-4:],  # ID Generator (our data's ID's were varchars to begin with)
                    n["name"], n["type"], n["reused"], n["manufacturer"], n["mass_kg"], n["mass_lb"], n["orbit"], n["reference-system"], n["regime"])

        cur.execute('INSERT INTO payloads VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', new_tuple)
        con.commit()

        payloads = cur.execute("SELECT * FROM payloads ORDER BY name ASC").fetchall()
        return render_template("payloads.html", payloads=payloads)

@views.route('/cores', methods=['GET', 'POST'])
def cores():
    con = sqlite3.connect(current_app.config["db"])
    con.row_factory = sqlite3.Row
    cur = con.cursor() 
    cores = cur.execute("SELECT * FROM cores").fetchall()
    return render_template("cores.html", cores=cores)

@views.route('/capsules', methods=['GET', 'POST'])
def capsules():
    con = sqlite3.connect(current_app.config["db"])
    con.row_factory = sqlite3.Row
    cur = con.cursor() 
    cores = cur.execute("SELECT * FROM capsules").fetchall()
    return render_template("capsules.html", capsules=capsules)
