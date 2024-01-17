#!/user/bin/python3

##   Exploring redirection with a simple Flask server. This server has
  ## the following endpoints:
   
  ## /admin            - returns 200 + 'Hello Admin'
  ## /guest/<guesty>   - returns 200 + 'Hello {guesty} Guest'
  ## /user/<name>      - returns 302 to one of the other 2 endpoints depending on the
  ##                    <name> provided."""

from flask import Flask
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<guesty>")
def hello_guest(guesty):
    return f"Hellow {guesty} Guest"


@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guesty = name))
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

