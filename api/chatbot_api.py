import flask
from flask_restful import Resource
from flask import request, jsonify, redirect, Response
from models.models import *


class ChatbotAPI(Resource):
    def get(self):
        #TODO Return chatbot data (list of all or specific id)
        return Response(status=200)
        
    def post(self):
        #TODO Promt a bot with id
        return Response(status=200)
    
    def delete(self):
        # Delete chatbot with id
        return Response(status=200)