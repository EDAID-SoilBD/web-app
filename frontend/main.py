#!/usr/bin/env python3

from flask import Flask, render_template, request
from requests import get

app = Flask(__name__)


@app.route("/")
def landing_page():
    return render_template("landing_page.html")


@app.route("/browse")
def browse_data():
    r = get("http://localhost:5000/api/data").json()
    return render_template("browse.html", records=r, colnames=r[0].keys())


@app.route("/search-data", methods=["GET"])
def search_data():
    payload = dict(request.args)
    r = get(f"http://localhost:5000/api/data", params=payload).json()
    print(r)
    return render_template("browse.html", records=r, colnames=r[0].keys())


@app.route("/search")
def search_page():
    return render_template("search.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)
