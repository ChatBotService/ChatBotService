import flask
from flask_restful import Resource
from flask import request, jsonify, redirect, Response
from models.models import *


class ConversationAPI(Resource):
    def get(self):
        if "id" in request.args:
            conversations = ConversationFile.query.filter_by(id=request.args["id"]).first()
            conversation_schema = ConversationFileSchema(many=False)
            return jsonify(conversation_schema.dump(conversations))
        else:
            conversations = ConversationFile.query.all()
            conversation_schema = ConversationFileSchema(many=True)
            return jsonify(conversation_schema.dump(conversations))
        
    def post(self):
        if request.files:
            uploaded_file = request.files["conversation-file"]
            print("Uploaded file", flush=True)
            print(uploaded_file, flush=True)
            conversation_file = ConversationFile(
                name=uploaded_file.filename,
                data=uploaded_file.read(),
                user_id = 0) #TODO: Hardcoded user id
            db.session.add(conversation_file)
            db.session.commit()
        return redirect("/dashboard")
    
    def delete(self):
        id = request.args.get("id")
        if id:
            ConversationFile.query.filter_by(id=id).delete()
            db.session.commit()
        return Response(status=200)