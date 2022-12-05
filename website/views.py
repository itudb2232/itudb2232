# This file is for arranging which pages the user can navigate to (i.e. launchpads, launches, rockets, ships...) #
# This file is a blueprint, it has a bunch of roots and urls inside of it #

from flask import Blueprint, render_template, current_app
import sqlite3

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/launches')
def launches():
    return render_template("launches.html")

@views.route('/launchpads')
def launchpads():
    return render_template("launchpads.html")

@views.route('/rockets')
def rockets():
    con = sqlite3.connect(current_app.config["db"])
    con.row_factory = sqlite3.Row  # Query returns objects
    cur = con.cursor() 
    rockets = cur.execute("SELECT * FROM rockets").fetchall()
    return render_template("rockets.html", rockets=rockets)

@views.route('/ships')
def ships():
    return render_template("ships.html")

@views.route('/payloads')
def payloads():
    con = sqlite3.connect(current_app.config["db"])
    con.row_factory = sqlite3.Row  # Query returns objects
    cur = con.cursor() 
    payloads = cur.execute("SELECT * FROM payloads").fetchall()
    print(payloads)
    return render_template("payloads.html", payloads=payloads)