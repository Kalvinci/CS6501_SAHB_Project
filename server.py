from flask import Flask, render_template, jsonify
from actuator import actuate, turnOff
app = Flask(__name__)

@app.route("/")
def root():
	return render_template("index.html")

@app.route("/working")
def working():
	return actuate("working")

@app.route("/reading")
def reading():
	return actuate("reading")

@app.route("/meeting")
def meeting():
	return actuate("meeting")

@app.route("/powerOff")
def powerOff():
	return turnOff()

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")