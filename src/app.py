from flask import Flask, request

from CSVReader import TruckReader
from FoodTrucks import FoodTrucks

app = Flask(__name__)

foodTrucks = FoodTrucks(TruckReader('/home/lilnaynay22/take-home-engineering-challenge/Mobile_Food_Facility_Permit.csv'))

@app.route("/location/<locationid>", methods=['GET'])
def getLocation(locationid):
  res = foodTrucks.getTrucksByLocation(locationid)
  if res:
    return {'data': res}, 200
  else:
    return "Location not found", 400

@app.route("/block/<block>", methods=['GET'])
def getBlock(block):
  res = foodTrucks.getTrucksByBlock(block)
  if res:
    return {'data': res}, 200
  else:
    return "Block not found", 400

@app.route("/add", methods=['POST'])
def addTruck():
  data = request.form
  res = foodTrucks.addTruck(data)
  if res[1]:
    return res[0], 200
  return res[0], 400