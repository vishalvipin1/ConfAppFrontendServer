from flask import Flask, render_template
from collections.abc import Mapping
import pyrebase

config = {
    "apiKey": "AIzaSyCKROkOh5vihJBh8CSQb0Lx1lEL-8hdfhQ",
    "authDomain": "voicevoip-3301b.firebaseapp.com",
   "databaseURL": "https://voicevoip-3301b-default-rtdb.firebaseio.com",
    "projectId": "voicevoip-3301b",
    "storageBucket": "voicevoip-3301b.appspot.com",
    "appId": "1:296053302562:web:ffc9da22a97601426eb17b",
}

firebase=pyrebase.initialize_app(config)



app=Flask(__name__)

@app.route('/')
def index():
    return render_template("another.html")

if(__name__=="__main__"):
    app.run(debug=True)