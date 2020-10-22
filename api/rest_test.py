import flask
from flask_restful import Resource
from flask import request, jsonify

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

class TestResource(Resource):
    def get(self):
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            return "<h1>This is a test API.</h1><br>Error: No id field provided. Please specify an id."
        results = []

        for book in books:
            if book['id'] == id:
                results.append(book)
        
        return jsonify(results)
