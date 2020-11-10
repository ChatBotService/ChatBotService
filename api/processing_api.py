import flask
from flask_restful import Resource
from flask import request, jsonify, redirect, Response
from models.models import *
from util import processing

class ProcessingAPI(Resource):
    def get(self):
        #Return current processing queue status
        conversation_schema = ConversationFileSchema(many=True)
        return jsonify(conversation_schema.dump(processing.processing_queue))
        
    def post(self):
        # Add process to queue
        file_id = request.args.get("id")
        if file_id:
            conversations = ConversationFile.query.filter_by(id=file_id).first()
            if conversations:
                for existing in processing.processing_queue:
                    if existing.id == int(file_id):
                        return Response(f"File with id {file_id} already in queue.",status=200)  
                processing.processing_queue.append(conversations)
                return Response(f"File with id {file_id} was added to queue.",status=200)
            else:
                return Response("Bad Request:\nCould not find or load existing conversation file.",status=400)
        else:
            return Response("Bad Request:\nCould not find or load existing conversation file.",status=400)
    
    def delete(self):
        # Remove a process from queue
        file_id = request.args.get("id")
        if file_id:
            for i in range(len(processing.processing_queue)):
                if processing.processing_queue[i].id == int(file_id):
                    del processing.processing_queue[i]
                    break
        return Response(status=200)