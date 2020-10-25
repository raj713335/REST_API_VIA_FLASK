from flask import Flask,request
from flask_restful import Resource,Api
import time
import threading
from functools import wraps
from datetime import datetime
import requests

app=Flask(__name__)
api=Api(app)

def time(function=None):

    @wraps(function)
    def wrapper(*args,**kwargs):
        s=datetime.now()
        _=function(*args,**kwargs)
        e=datetime.now()
        print("Execution Time: {}".format(e-s))

        return _
    return wrapper


def monitor(function=None):
    @wraps(function)
    def wrapper(*args,**kwargs):
        _=function(*args,**kwargs)
        print(("Ip Address : {}".format(request.remote_user)))
        print("Cookies : {} ".format(request.cookies))
        print("User Agent : {}".format(request.user_agent))
        print("Remote User : {} ".format(request.remote_user))
        return _
    return wrapper




class HelloWorld(Resource):

    @monitor
    def get(self):


        return {'hello':'world'}

api.add_resource(HelloWorld,'/')

if __name__=="__main__":
    app.run(debug=True)
