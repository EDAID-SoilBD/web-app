#!/usr/bin/env python3

from flask import Flask, render_template
from requests import get

app = Flask(__name__)


@app.route("/")
def landing_page():
    return render_template("landing_page.html")


@app.route("/browse")
def browse_data():
    r = get("http://localhost:5000/data").json()
    return render_template("browse.html", records=r, colnames=r[0].keys())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)
