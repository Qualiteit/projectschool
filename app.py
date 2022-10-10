from flask import Flask, render_template, Response, request, redirect, url_for
from djitellopy import Tello
from utils import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/dronetakeoff', methods=['GET', 'POST'])
def connect():
    print('connecting to drone')
    try:
        drone.connect()
        print('The drone is connected!')
        drone.takeoff()
    except:
        print('something went wrong')
    return render_template("index.html")