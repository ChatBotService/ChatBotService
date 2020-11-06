import flask
from flask_restful import Resource
from flask import request, jsonify, redirect, Response
from models.models import *
from util import processing

class ProcessingAPI(Resource):
    def get(self):
        #TODO Return current processing queue status
        return jsonify({ "queue_size":len(processing.processing_queue) })
        
    def post(self):
        file_id = request.args.get("id")
        if file_id:
            conversations = ConversationFile.query.filter_by(id=file_id).first()
            if conversations:
                processing.processing_queue.append(file_id)
                return Response(f"File with id {file_id} was added to queue.",status=200)
            else:
                return Response("Bad Request:\nCould not find or load existing conversation file.",status=400)
        else:
            return Response("Bad Request:\nCould not find or load existing conversation file.",status=400)
    
    def delete(self):
        # Remove a process from queue
        return Response(status=200)