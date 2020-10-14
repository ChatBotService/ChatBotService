from flask import Flask

visitors = 0

app = Flask(__name__)
@app.route("/")
def index():
    global visitors
    visitors += 1
    return f"Hello World!<br>Visitors: {visitors}"

def run():
    app.run(host="0.0.0.0", port=80, debug=True)