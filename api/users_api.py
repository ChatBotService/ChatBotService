import flask
from flask_restful import Resource
from flask import request, jsonify, redirect, Response
from models.models import *


class UsersAPI(Resource):
    def get(self):
        if "id" in request.args:
            users = User.query.filter_by(id=request.args["id"]).first()
            users_schema = UserSchema(many=False)
            return jsonify(UserSchema.dump(users))
        else:
            users = User.query.all()
            users_schema = UserSchema(many=True)
            return jsonify(users_schema.dump(users))
        
    def post(self):
        if request.files:
            uploaded_file = request.files["conversation-file"]
            print("Uploaded file", flush=True)
            print(uploaded_file, flush=True)
            file_blob = uploaded_file.read()
            conversation_file = ConversationFile(
                name=uploaded_file.filename,
                data=file_blob,
                data_size=len(file_blob),
                user_id = 0) #TODO: Hardcoded user id
            db.session.add(conversation_file)
            db.session.commit()
        return Response(status=200)
    
    def delete(self):
        id = request.args.get("id")
        if id:
            ConversationFile.query.filter_by(id=id).delete()
            db.session.commit()
        return Response(status=200)