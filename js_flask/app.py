from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route("/api", methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        dummy_json = {
            "test": "test"
        }
        return jsonify(dummy_json)

    if request.method == 'POST':
        response = request.values
        return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
