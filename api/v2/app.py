from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)




#Register a user
@app.('/route/auth/signup', methods=['POST']

pass

#Login a user
 @app.('/auth/login', methods=['POST']

pass

#Fetch all questions
@app.('/questions', methods=['GET']

pass

#Fetch a specific question
@app.('/questions/<questionId>', methods=['GET']

pass

#Post a question
@app.('/questions', methods=['POST']

pass

#Delete a question
@app.('/questions/<questionId>', methods=['DELETE']

pass

#Post an answer to a question
@app.('/questions/<questionId>/answers', methods=['POST']

pass


#Mark an answer as accepted or update an answer.
@app.('/questions/<questionId>/answers/<answerId>', methods=['PUT']

pass
