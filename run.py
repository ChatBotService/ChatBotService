from flask import Flask, render_template
from flask_restful import Api
from api.rest_test import TestResource
print("Running...")

app = Flask(__name__)
api = Api(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.config["DEBUG"] = True

api.add_resource(TestResource,"/test", "/test/<int:id>")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


app.run(host="0.0.0.0", port=80, debug=True)