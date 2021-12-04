from flask import Flask, render_template, jsonify
from actuator import actuate, turnOff
app = Flask(__name__)

@app.route("/")
def root():
	return render_template("index.html")

@app.route("/working")
def working():
	sensed_data = actuate("working")
	return jsonify(sensed_data)

@app.route("/reading")
def reading():
	sensed_data = actuate("reading")
	return jsonify(sensed_data)

@app.route("/meeting")
def meeting():
	sensed_data = actuate("meeting")
	return jsonify(sensed_data)

@app.route("/powerOff")
def powerOff():
	turnOff()
	return "SUCCESS"

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")