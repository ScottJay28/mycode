#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   A simple Flask server. This server has the following endpoints:
   
   /success/<name> - responds with 200 + 'Welcome {name}'
   
   /
   /start          - Both endpoints respond with 200 + postmaker.html (template)
   
   /login          - a POST will have the form read for 'nm'
                   - a GET will be scanned for the query param ?nm=some_value"""

# python3 -m pip install flask
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}\n"

@app.route("/")
@app.route("/start")
def start():
    return render_template("postmaker.html")
# This is where postmaker.html POSTs data to
# A user could also browser (GET) to this location

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form.get("nm")
        else:
            user = "defaultuser"
    elif request.method = "GET":
        if request.args.get("nm")
        else:
            user = "defaultuser"
    return redirect(url_for("success", name = user))
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
