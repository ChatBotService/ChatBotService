import flask
from flask_restful import Resource
from flask import request, jsonify, redirect, Response
from models.models import *


class ChatbotAPI(Resource):
    def get(self):
        if "id" in request.args:
            model = TrainedModel.query.filter_by(id=request.args["id"]).first()
            model_schema = TrainedModelSchema(many=False)
            return jsonify(model_schema.dump(model))
        elif "file_id" in request.args:
            model = TrainedModel.query.filter_by(file_id=request.args["file_id"]).all()
            conversation_schema = TrainedModelSchema(many=True)
            return jsonify(model_schema.dump(model))
        else:
            model = TrainedModel.query.all()
            model_schema = TrainedModelSchema(many=True)
            return jsonify(model_schema.dump(model))
        
    def post(self):
        #TODO Promt a bot with id
        return Response(status=200)
    
    def delete(self):
        # Delete chatbot with id
        return Response(status=200) 