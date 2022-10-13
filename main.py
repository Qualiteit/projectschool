from flask import Flask, render_template, Response, request, redirect, url_for
from djitellopy import Tello
from utils import *

drone = initializeTello()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/takeoff', methods=['GET', 'POST'])
def takeoff():
    print('connecting to drone')
    try:
        drone.connect()
        print('The drone is connected!')
        drone.takeoff()
        drone.land()
    except:
        print('something went wrong')
    return render_template("index.html")
    
@app.route('/land', methods=['GET', 'POST'])
def land():
    print('land to drone')
    try:
        drone.connect()
        print('The drone is connected!')
        drone.takeoff()
        drone.land()
    except:
        print('something went wrong')
    return render_template("index.html")
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)