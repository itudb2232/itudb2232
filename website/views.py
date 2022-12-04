# This file is for arranging which pages the user can navigate to (i.e. launchpads, launches, rockets, ships...) #
# this file is a blueprint, it has a bunch of roots and urls inside of it #

from flask import Blueprint

views = Blueprint('views', __name__)

# The functions below will return html files later on, these h1 tags are just placeholders #

@views.route('/')
def home():
    return "<h1 align = 'center'>You have landed on our webpage!</h1>"

@views.route('/launches')
def launches():
    return "<h1>Launches Page</h1>"

@views.route('/launchpads')
def launchpads():
    return "<h1>Launchpads Page</h1>"

@views.route('/rockets')
def rockets():
    return "<h1>Rockets Page</h1>"

@views.route('/ships')
def ships():
    return "<h1>Ships Page</h1>"