from flask import Flask, render_template, Response, request, redirect, url_for
from djitellopy import Tello
import cv2
import numpy as np
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/takeoff', methods=['GET', 'POST'])
def connect():
    print('Drone is taking off')
    try:
        myDrone.connect()
        print('The drone is connected!')
        myDrone.takeoff()
    except:
        print('something went wrong')
    return render_template("index.html")