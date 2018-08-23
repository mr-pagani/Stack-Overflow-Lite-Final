import unittest
import json
import os

from v1 import app

class TestEndpoints(unittest.TestCase):

    def test_returnall(self):
        resp = self.app.get('/questions')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_post_question(self):
        post_data = {
			"id": 5,
			"answer": "none",
            "name": "question12"
            }
        resp = self.app.post('/questions', data=json.dumps(post_data),
        content_type='application/json')

        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.content_type, 'application/json')


    def test_get_unique_question(self):
        resp = self.app.get('/questions/42')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_post_answer(self):
        pass

if __name__ == '__main__':
    unittest.main()
