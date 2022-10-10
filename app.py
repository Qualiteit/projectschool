from flask import Flask, render_template, Response, request, redirect, url_for
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
