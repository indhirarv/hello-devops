from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello DevOps – Running on AWS EC2 (Ubuntu) 🚀"

app.run(host="0.0.0.0", port=80)

