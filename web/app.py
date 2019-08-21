from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_api import status
from pymongo import MongoClient
from operator import itemgetter
import itertools
import json

import pandas as pd
import datetime
import numpy as np

app = Flask(__name__)
api = Api(app)

trukers = MongoClient("mongodb://db:27017")
db = trukers.registration
drivers = db["drivers"]

def truck(value):
    list = ["Não Informado", "Caminhão 3/4", "Caminhão Toco", "Caminhão Truck", "Carreta Simples", "Carreta Eixo Extendido"]
    return list[value].lower()

@app.route("/api/truck_driver",methods=["POST"])
def truck_driver():
    try:
        body = request.get_json()
        record_created = drivers.insert(body)
        return jsonify({"ObjectId": record_created}), status.HTTP_201_CREATED
    except Exception as e:
         return jsonify({"message" :  str(e)}), status.HTTP_500_INTERNAL_SERVER_ERROR

@app.route("/api/drivers")
def all_drivers():
    output = []
    all_drivers = drivers.find().sort("name")

    for s in all_drivers:
        output.append({'name' : s['name'], 'age': s['age'], 'truck_type_id': s['truck']['type'],'truck_type_label': truck(s['truck']['type'])})

    return jsonify({"drivers": output, "total": all_drivers.count()}), 201

@app.route("/api/owner_truck")
def owner_truck():
    output = []
    owner_truck = drivers.find({ "owner_truck" : True }).sort("name")
    for s in owner_truck:
        output.append({'name' : s['name'], 'truck_type_id': s['truck']['type'], 'truck_type_label': truck(s['truck']['type'])})

    if  owner_truck.count() <= 0:
        return jsonify({"message":"Records not found!"}), status.HTTP_200_OK
    else:
        return jsonify({'owner_truck' : output, "total": owner_truck.count()}), status.HTTP_200_OK

@app.route("/api/truckempty")
def truckload():
    output = []
    truckempty = drivers.find({ "truckload" : False }).sort("name")
    for s in truckempty:
        output.append({'driver' : s['name'], 'truck_type_id': s['truck']['type'],'truck_type_label': truck(s['truck']['type']), 'road_trip': s['road_trip']})

    if truckempty.count() <= 0:
        return jsonify({"message":"Records not found!"}), status.HTTP_200_OK
    else:
        return jsonify({'truck_empty' : output, "total": truckempty.count()}), status.HTTP_200_OK

@app.route("/api/geolocation_by_truck_type")
def geolocation():
    geolocation = drivers.find()
    output = []
    by_truck_type = []

    for s in geolocation:
        output.append({'driver' : s['name'], 'truck_type_id': s['truck']['type'], 'truck_type_label': truck(s['truck']['type']), "road_trip": s['road_trip']}) 

    sorted_output = sorted(output, key=itemgetter('truck_type_id'))
    for key, group in itertools.groupby(sorted_output, key=lambda x:x['truck_type_id']):
        by_truck_type.append({ "type_" + str(key) : list(group)})

    if  geolocation.count() <= 0:
        return jsonify({"message":"Records not found!"}), status.HTTP_200_OK
    else:
        return jsonify({'geolocation_by_truck_type' : by_truck_type, "total": geolocation.count()}), status.HTTP_200_OK

@app.route("/api/update_driver")
def update():

    return jsonify({"message":"Records not found!"}), status.HTTP_200_OK


@app.route("/api/report")
def report():
    output = []
    value = []
    report = drivers.find().sort("name")

    for s in report:
        output.append(s['date'])
        value.append(1)

    df = pd.DataFrame({ "date" : output, "value": value })
    df.date = pd.to_datetime(df.date)
    dg = df.groupby(pd.Grouper(key='date', freq='1M')).sum()
    dg.index = dg.index.strftime('%B')
    mounth = dg.to_json(orient='index')
    dg = df.groupby(pd.Grouper(key='date', freq='1W')).sum()
    dg.index = dg.index.strftime('%A')
    week = dg.to_json(orient='records')
    dg = df.groupby(pd.Grouper(key='date', freq='1D')).sum()
    dg.index = dg.index.strftime('%A')
    day = dg.to_json(orient='records')

    return jsonify({"day":json.loads(day), "week": json.loads(week), "month": json.loads(mounth)}), 201

@app.route('/')
def root():
    return jsonify({"title":"Teste Backend", "author": "Adriano Souza"})

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)

    