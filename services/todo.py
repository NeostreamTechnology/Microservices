from flask import Flask ,jsonify, make_response
import json
import os

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

with open('{}/database/todo.json'.format(database_path),"r") as f:
	todo_list = json.load(f)

@app.route('/',methods=['GET'])
def hello():
	return "Todo service is up and running"

"""Display all the list"""
@app.route('/lists',methods=['GET'])
def show_lists():
	tdlist=[]
	for username in todo_list:
		for name in todo_list[username]:
			tdlist.append(name)
	return jsonify(lists=tdlist)

'''Return a userdefined list'''
@app.route('/lists/<username>',methods=['GET'])
def user_list(username):
	if username not in todo_list:
		return "No lists found"
	return jsonify(todo_list[username])


if __name__=="__main__":
	app.run(port=5001,debug=True)
