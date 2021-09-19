from flask import Flask, request, jsonify, abort

app = Flask(__name__)
# app.config.from_object("config.Config")

@app.route("/")
def index():
    return "Hello World"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
