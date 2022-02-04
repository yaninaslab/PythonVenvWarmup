from os import stat_result
import dbinteractions as dbi
import getpass as gp
from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.get('/')
def hello_world():
    print(request)
    return "Hello World"


@app.post('/login')
def attempt_login():
    username = request.json['username']
    password = request.json['password']

    login_success, user_id = dbi.attempt_login(username, password)

    if(login_success == True):
        dogs = dbi.list_your_dogs(user_id)
        dogs_json = json.dumps(dogs, default=str)
        return Response(dogs_json, mimetype="application/json", status=200)

    else:
        return Response("Authentication error", mimetype="plain/text", status=403)


app.run(debug=True)
