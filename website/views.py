# This file is for arranging which pages the user can navigate to (i.e. launchpads, launches, rockets, ships...) #
# This file is a blueprint, it has a bunch of roots and urls inside of it #

from flask import Blueprint, render_template, current_app, request
import sqlite3

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/launches', methods=['GET', 'POST'])
def launches():
    return render_template("launches.html")

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

@views.route('/ships', methods=['GET', 'POST'])
def ships():
    con = sqlite3.connect(current_app.config["db"])
    con.row_factory = sqlite3.Row  
    cur = con.cursor() 
    if request.method == 'POST':
        type = request.form['type']
        cur.execute('SELECT * FROM ships WHERE type = ?', (type,))
        ships = cur.fetchall()
    else:
        ships = cur.execute("SELECT * FROM ships").fetchall()
    return render_template("ships.html",ships=ships)

@views.route('/ships/ship_details_2', methods=['GET', 'POST'])
def ship_details_2():
    con = sqlite3.connect(current_app.config["db"])
    con.row_factory = sqlite3.Row  
    cur = con.cursor() 
    ship_details_2 = cur.execute("SELECT * FROM ship_details_2").fetchall()
    return render_template("ship_details_2.html",ship_details_2=ship_details_2)

@views.route('/payloads', methods=['GET', 'POST'])
def payloads():
    con = sqlite3.connect(current_app.config["db"])
    con.row_factory = sqlite3.Row  # Query returns objects
    cur = con.cursor() 
    payloads = cur.execute("SELECT * FROM payloads").fetchall()
    insert_data = request.form
    print(insert_data)
    return render_template("payloads.html", payloads=payloads)

