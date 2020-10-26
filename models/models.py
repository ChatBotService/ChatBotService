from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    conversation_files = db.relationship("ConversationFile")

class ConversationFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    creation_date = db.Column(db.DateTime, default=datetime.now)
    data = db.Column(db.LargeBinary)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    models = db.relationship("TrainedModel")

class TrainedModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    creation_date = db.Column(db.DateTime, default=datetime.now)
    data = db.Column(db.LargeBinary)
    file_id = db.Column(db.Integer, db.ForeignKey("conversation_file.id"))

def init_db():
    user1 = User(id=0)
    db.session.add(user1)
    user2 = User(id=1)
    db.session.add(user2)
    db.session.commit()