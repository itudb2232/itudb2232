# This file is for arranging which pages the user can navigate to (i.e. launchpads, launches, rockets, ships...) #
# This file is a blueprint, it has a bunch of roots and urls inside of it #

from flask import Blueprint, render_template

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
    return render_template("rockets.html")

@views.route('/ships')
def ships():
    return render_template("ships.html")