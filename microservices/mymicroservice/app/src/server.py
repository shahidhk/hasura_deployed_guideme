from src import app
from flask import jsonify, request
import requests
import json

@app.route('/')
def index():
    return "Index Page"

def func_for_face(f):
    #print f
    return "1"

@app.route('/facerecognize', methods=['POST'])
def index1():
    #print request.json
    imgURL = request.json["photourl"]
    print("URL : " + imgURL)
    p = FaceDetect(imgURL)
    a = p.detect()
    return jsonify({'id': a}), 201
