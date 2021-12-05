from flask import Flask, render_template, jsonify
from actuator import actuate, turnOff
app = Flask(__name__)

@app.route("/")
def root():
	return render_template("index.html")

@app.route("/working")
def working():
	return_code = actuate("working")
	return jsonify("SUCCESS" if return_code == 0 else "FAILED")

@app.route("/reading")
def reading():
	return_code = actuate("reading")
	return jsonify("SUCCESS" if return_code == 0 else "FAILED")

@app.route("/meeting")
def meeting():
	return_code = actuate("meeting")
	return jsonify("SUCCESS" if return_code == 0 else "FAILED")

@app.route("/powerOff")
def powerOff():
	return_code = turnOff()
	return jsonify("SUCCESS" if return_code == 0 else "FAILED")

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")