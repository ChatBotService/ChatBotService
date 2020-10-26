import flask
from flask_restful import Resource
from flask import request, jsonify, redirect
from models.models import *


class BotCreation(Resource):
    def get(self):
        return redirect("/dashboard")
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
