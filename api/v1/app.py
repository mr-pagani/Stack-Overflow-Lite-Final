from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)



questions = [
	{
	    "id": 42,
	    "name": "Question",
	    "answer": "Answer"
	}

]


@app.route('/questions/', methods=['GET'])
def returnall():
    return jsonify({'questions' : questions}), 200

@app.route('/questions', methods=['POST'])
def post_question():
	request_data = request.get_json()
	new_question = {
		"id":request_data["id"],
		"name":request_data["name"],
		"answer":request_data["answer"]
			}
	questions.append(new_question)
	return jsonify(new_question), 201


@app.route('/questions/<int:id>', methods=['GET'])
def get_unique_question(id):
	for question in questions:
		if question ["id"] == id:
			return jsonify(question)
		return ("Question not found"), 404


@app.route('/questions/<int:id>/answers', methods=['POST'])
def post_answer(id):
	for question in questions:
		if question ["id"] == id:
			request_data = request.get_json()
			new_answer = {
				"id":id,
				"name":"name",
				"answer":request_data["answer"]
					}
			questions.append(new_answer)
			return jsonify(new_answer), 201
		return ("Question with id not found"), 404

app.run(debug=True)
