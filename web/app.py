from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_api import status
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

trukers = MongoClient("mongodb://db:27017")
db = trukers.registration
drivers = db["drivers"]

class UnloadedDriver(Resource):
    def get(self):
        body = {
            'UnloadedDriver': 1000
        }
        return jsonify(body)

class OwnVehicle(Resource):
    def get(self):
        body = {
            'OwnVehicle': 233
        }
        return jsonify(body)  

api.add_resource(UnloadedDriver, "/unloaded_driver")
api.add_resource(OwnVehicle, "/own_vehicle")

@app.route("/truck-driver",methods=["POST"])
def truck_driver():
    body = request.get_json()
    drivers.insert({ "driver": body })
    return jsonify({"message": "Driver " + body["name"] + " created with sueccess!"}), status.HTTP_201_CREATED

@app.route('/')
def root():
    return jsonify({"title":"Teste Backend", "author": "Adriano Souza"})

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)