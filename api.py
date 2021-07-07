from flask import Flask, json, request, jsonify, render_template, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import time
from backend.HelloApiHandler import HelloApiHandler

# app = Flask(__name__)
app = Flask(__name__, static_url_path='', static_folder='app/build')
CORS(app)
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

# Test function to invoke a Flask Endpoint from React
@app.route('/time')
def get_current_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return {'time' : current_time}

api.add_resource(HelloApiHandler, '/flask/hello')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4200, debug=True)

