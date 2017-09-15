from flask import Flask, jsonify, make_response
import requests
import os
import simplejson as json

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
#import the users database in the service and parseit as json file
with open ("{}/database/users.json".format(database_path), "r") as f:
	usr = json.load(f)


#write our application endpoints

@app.route("/",methods=['GET'])
def hello():
	return "Hey you! the service is up and running!!"

'''Get the list of users'''
@app.route("/users",methods=['GET'])
def users():
	resp= make_response(json.dumps(usr,sort_keys=True,indent=4))
	resp.headers['Content-Type']="application/json"
	return resp

'''Get info about a specific user'''
@app.route("/user/<username>",methods=['GET'])
def user(username):
	if username not in usr:
		return "Not found"
	return jsonify(usr[username])

'''Get list based on username'''
@app.route("/user/<username>/lists",methods=['GET'])
def user_lists(username):
	try:
		req=requests.get("http://127.0.0.1:5001/lists/{}".format(username))
	except requests.exceptions.ConnectionError:
		return "Service unavailable"
	return req.text

if __name__=="__main__":
	app.run(port=5000,debug=True)

