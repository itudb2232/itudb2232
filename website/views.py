# This file is for arranging which pages the user can navigate to (i.e. launchpads, launches, rockets, ships...) #
# This file is a blueprint, it has a bunch of roots and urls inside of it #

from flask import Blueprint, render_template, current_app, request, redirect, url_for
import sqlite3
from flask_login import current_user

from time import time_ns
from random import random

import forms
import database

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
    launch_data = database.get_launches()
    return render_template("launches.html", launches=launch_data)

@views.route('/launchpads', methods=['GET', 'POST'])
def launchpads():
    return render_template("launchpads.html")

@views.route('/rockets', methods=['GET', 'POST'])
def rockets():
    rocket_data = database.get_rockets()
    return render_template("rockets.html", rockets=rocket_data)

@views.route('/rockets/rocket_details_1', methods=['GET', 'POST'])
def rocket_details_1():
    rocket_d1 = database.get_rocket_d1()
    return render_template("rocket_details_1.html", rocket_details_1=rocket_d1)



@views.route('/ships', methods=['GET', 'POST'])
def ships():
    ship_data, ship_d1_data = database.get_ships(request)

    return render_template("ships.html",ships=ship_data, ship_details_1=ship_d1_data)



@views.route('/ships/ship_details_2', methods=['GET', 'POST'])
def ship_details_2():
    ship_d2_data = database.get_ship_d2()
    return render_template("ship_details_2.html",ship_details_2=ship_d2_data)

@views.route('/payloads', methods=['GET', 'POST'])
def payloads():
    if request.method == "GET":
        payload_data = database.get_payloads()
        return render_template("payloads.html", payloads=payload_data)
    else:
        database.add_payload(request)

        payload_data = database.get_payloads()
        return render_template("payloads.html", payloads=payload_data)

@views.route('/cores', methods=['GET', 'POST'])
def cores():
    core_data = database.get_cores()
    return render_template("cores.html", cores=core_data)

@views.route('/capsules', methods=['GET', 'POST'])
def capsules():
    capsule_data = database.get_capsules()
    return render_template("capsules.html", capsules=capsule_data)
