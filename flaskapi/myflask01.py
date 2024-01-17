#!/user/bin/python3

# an object of flask class is our WSGI application
from flask import Flask

#Flask constructor takes the name of current module (__name__) as argument

app = Flask(__name__)

#route() function of the Flask class is a decorator. tells application which URL should call the function

@app.route("/")
def hello_world():
    return "Hello World"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) 

