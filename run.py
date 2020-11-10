from flask import Flask, render_template, request, redirect
# Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
# Models
from models.models import db, ma
from models.models import *

# APIs
from api.rest_test import TestResource
from api.conversation_api import ConversationAPI
from api.chatbot_api import ChatbotAPI
from api.processing_api import ProcessingAPI


import os

print("Running...", flush=True)

app = Flask(__name__)
api = Api(app)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False
app.config["DEBUG"] = True

# Database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db_path = os.path.join(os.path.dirname(__file__), 'botstorage.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db.init_app(app)
ma.init_app(app)

# with app.app_context():
#     db.drop_all()
#     db.create_all()
#     from models import models
#     models.init_db()


# APIs
api.add_resource(TestResource,"/test", "/test/<int:id>")
api.add_resource(ConversationAPI,"/conversation", "/conversation")
api.add_resource(ChatbotAPI,"/chatbot", "/chatbot")
api.add_resource(ProcessingAPI,"/process", "/process")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if request.method == "POST" and request.files:
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
    
    user_conversations = ConversationFile.query.filter_by(user_id=0).all()
    return render_template("dashboard.html", user_conversations=user_conversations)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)