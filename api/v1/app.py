from flask import Flask, jsonify
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
			

@app.route('/questions/all', methods=['GET'])
def returnall():
    return jsonify({'questions' : questions})

class Question(Resource):

    def get(self, question):
        for question in questions:
            if(question == question["name"]):
                return question, 200
        return "Question not found", 404

    def post(self, question):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("answer")
        args = parser.parse_args()

        for question in questions:
            if(question == question["name"]):
                return "Question {} already exists".format(question), 400

        question = {
        	"id": args["id"],
            "name": name,
            "answer": args["answer"]
        }
        questions.append(question)
        return question, 201

    def put(self, question):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("answer")
        args = parser.parse_args()

        for question in questions:
            if(question == question["name"]):
                question["id"] = args["id"]
                question["answer"] = args["answer"]
                return question, 200
        
        question = {
        	"id": args["id"],
            "name": question,
            "answer": args["answer"]
        }
        questions.append(question)
        return question, 201

    def delete(self, question):
        global questions
        question = [question for question in questions if question["name"] != question]
        return "{} is deleted.".format(question), 200
      
api.add_resource(Question, "/questions/<string:question>")

app.run(debug=True)