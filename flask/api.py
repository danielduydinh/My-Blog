from flask import Flask, json, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello World!"

# Test function to invoke a Flask Endpoint from React
@app.route('/time')
def get_current_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return {'time' : current_time}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4200, debug=True)

