import flask
from flask_restful import Resource
from flask import request, jsonify, redirect, Response
from models.models import *


class ProcessingAPI(Resource):
    def get(self):
        #TODO Return current processing queue status
        return Response(status=200)
        
    def post(self):
        #TODO Add uploaded file to processing queue
        return Response(status=200)
    
    def delete(self):
        # Remove a process from queue
        return Response(status=200)