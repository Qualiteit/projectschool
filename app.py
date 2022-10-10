from flask import Flask, render_template, Response, request, redirect, url_for
from djitellopy import Tello
app = Flask(__name__)

def parse_args(args):

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
