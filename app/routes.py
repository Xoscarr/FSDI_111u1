from flask import Flask, request 
from datetime import datetime 
#from the flask module import the Flask class. 

app = Flask(__name__)
#instantiating the Flask class into the app variable 

PHONEBOOK = {
    "Oscar": {
        "last_name":"Rodriguez",
        "numbers":[
            "555-555-5555",
            "777-777-7777"
            ],
        
    },
    "Angel":{
        "last_name":"Garica",
        "numbers": [
            "111-111-1111",
            "222-222-2222"

        ],
        
    }, 
    "Gary":{
        "last_name":"Galvin",
        "numbers":[
            "999-999-999",
        ],
    }, 
}

@app.route("/")  # the route decorator 
def index():    # the wrapped function 
    return "<h1> Oscar Rodriguez</h1>" # The return statment 


@app.route("/version")
def get_version():
    timestamp = datetime.now().strftime("%F %H:%M:%S")
    out = {
        "version": "1.0.0",
        "server_time": timestamp,
        "ok": True
    }
    return out 

@app.route("/numbers/<name>")
def get_numbers(name):
    out = PHONEBOOK.get(name, {})
    return out 


@app.route("/numbers")
def get_all_numbers():
    return PHONEBOOK


@app.route("/numbers", methods=["POST"])
def add_number():
    number = request.json
    PHONEBOOK[number.get("name")] = number["data"] 
    return "OK", 204 