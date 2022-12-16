# This file is for arranging which pages the user can navigate to (i.e. launchpads, launches, rockets, ships...) #
# This file is a blueprint, it has a bunch of roots and urls inside of it #

from flask import Blueprint, render_template, current_app, request, redirect, url_for, flash
import sqlite3
from flask_login import current_user, login_user, logout_user, login_required

from time import time_ns
from random import random
import passlib.hash

import forms
import database
import users

views = Blueprint('views', __name__)

@views.route("/login", methods=["GET", "POST"])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        username = form.data["username"]
        user = users.get_user(username)

        if user is not None:
            password = form.data["password"]
            if passlib.hash.pbkdf2_sha256.verify(password, user.password):
                login_user(user)
                flash("Welcome to SpaceXhibit!")

                return redirect(url_for("views.home"))
            else:
                flash("Wrong password.")
        else:
            flash("You're not on the guest list. Why don't you sign up?")
    
    return render_template("login.html", form=form)

@views.route('/home')
@views.route("/")
def home():
    return render_template("home.html")

@views.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("views.home"))

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

@views.route('/payloads', methods=['GET'])
def payloads():
    payload_data = database.get_payloads()
    return render_template("payloads.html", payloads=payload_data)

@views.route('/add_payload', methods=['POST'])
@login_required
def add_payload():
    database.add_payload(request)
    return redirect(url_for("views.payloads"))

@views.route('/cores', methods=['GET', 'POST'])
def cores():
    core_data = database.get_cores()
    return render_template("cores.html", cores=core_data)

@views.route('/capsules', methods=['GET', 'POST'])
def capsules():
    capsule_data = database.get_capsules()
    return render_template("capsules.html", capsules=capsule_data)
