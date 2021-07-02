from flask import Flask, json, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    print("Hello World!")
    return "Hello World!"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4200, debug=True)

