from flask import Flask, jsonify, request
from flask_restful import Api, Resource
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

class Registration(Resource):
    def get(self):
        # REFACTORY
        body = {
            'driver': {
                'name': "Loren Ipsun",
                'age': 35,
                'gender': "masculino",
                'cnh': 'D',
                'vehicle' : {
                    'owner' : True,
                    'with_charge': False,
                    'type': 1
                }
            }
        }

        response = drivers.insert({
            "driver": body
        })
        
        return jsonify(body) 


api.add_resource(UnloadedDriver, "/unloaded_driver")
api.add_resource(OwnVehicle, "/own_vehicle")
api.add_resource(Registration, "/registration")

@app.route('/')
def root():
    return "<pre><b>TruckPad: Teste Backend</b><br />Author: <i>Adriano Souza</i></pre>"

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)