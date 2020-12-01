from flask import Flask, render_template, request, redirect
# Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
# Models
from models.models import db, ma
from models.models import *

# APIs
from api.rest_test import TestResource
from api.conversation_api import ConversationAPI
from api.chatbot_api import ChatbotAPI
from api.processing_api import ProcessingAPI

from util import processing

import os

print("Running...", flush=True)

app = Flask(__name__)
api = Api(app)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False
app.config["DEBUG"] = True

# Database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db_env = os.environ.get("DB_PATH")
print(db_env)
db_uri = db_env
print("Database uri: ", flush=True)
print(db_uri, flush=True)



engine = create_engine(db_uri)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db.init_app(app)
ma.init_app(app)

print("Initializing database...", flush=True)
# with app.app_context():
#     db.drop_all()
#     db.create_all()
#     from models import models
#     models.init_db()

print("Database initialized", flush=True)

processing.init_sessionfactory(engine)

# APIs
api.add_resource(TestResource,"/test", "/test/<int:id>")
api.add_resource(ConversationAPI,"/conversations", "/conversations")
api.add_resource(ChatbotAPI,"/chatbots", "/chatbots")
api.add_resource(ProcessingAPI,"/processes", "/processes")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    ui_action = request.form.get("ui-action")
    if request.method == "POST" and ui_action:
        if ui_action == "new-conversation" and request.files:
            uploaded_file = request.files["conversation-file"]
            print("Uploaded file", flush=True)
            print(uploaded_file, flush=True)
            conv_name = request.form.get("conversation_name")
            file_blob = uploaded_file.read()
            conversation_file = ConversationFile(
                name=conv_name,
                data=file_blob,
                data_size=len(file_blob),
                user_id = 0) #TODO: Hardcoded user id
            db.session.add(conversation_file)
            db.session.commit()
        elif ui_action == "new-bot":
            print("Creating new bot from conversation", flush=True)
            file_id = request.form.get("file_id")
            model_name = request.form.get("model_name")
            if file_id and model_name:
                #if not processing.in_queue(int(file_id)):
                conversation = ConversationFile.query.filter_by(id=int(file_id)).first()
                processing.add_to_queue({"conversation" : conversation, "name" : model_name})

    user_conversations = ConversationFile.query.filter_by(user_id=0).all()
    trained_models = []
    for conv in user_conversations:
        trained_models.extend(TrainedModel.query.filter_by(file_id=conv.id).all())
    return render_template("dashboard.html", user_conversations=user_conversations, trained_models=trained_models)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80, debug=True, use_reloader=False)