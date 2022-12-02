from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def landing_page():
    return "SpaceXhibit! (coming soon...)"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)

