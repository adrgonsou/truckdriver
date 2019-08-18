from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_api import status
from pymongo import MongoClient
import pandas as pd

app = Flask(__name__)
api = Api(app)

trukers = MongoClient("mongodb://db:27017")
db = trukers.registration
drivers = db["drivers"]

@app.route("/truck-driver",methods=["POST"])
def truck_driver():
    body = request.get_json()
    drivers.insert(body)
    return jsonify({"message": "Driver " + body["name"] + " created with sueccess!"}), status.HTTP_201_CREATED

@app.route("/owner_truck")
def owner_truck():
    output = []
    owner_truck = drivers.find({ "owner_truck" : True }).sort("name")
    for s in owner_truck:
        output.append({'name' : s['name'], 'truck_type': s['truck']['type']})

    return jsonify({'owner_truck' : output, "total": owner_truck.count()}), status.HTTP_200_OK

@app.route("/truckempty")
def truckload():
    output = []
    truckempty = drivers.find({ "truckload" : False }).sort("name")
    for s in truckempty:
        output.append({'name' : s['name'], 'truck_type': s['truck']['type'], 'road_trip': s['road_trip']})

    return jsonify({'truck_empty' : output, "total": truckempty.count()}), status.HTTP_200_OK

@app.route("/geolocation_by_truck_type")
def geolocation():
    
    output = drivers.aggregate({group : {_id : "truck", total : { sum : 1 }}})
    return jsonify({'geolocation_by_truck_type' : output, "total": geolocation.count()}), status.HTTP_200_OK

@app.route('/')
def root():
    return jsonify({"title":"Teste Backend", "author": "Adriano Souza"})

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)