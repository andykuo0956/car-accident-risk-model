from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from risk_model_v1 import risk_model
import geopandas as gpd

app = Flask(__name__)
CORS(app)

A1_traffic_accident_simple = gpd.read_file(
    "rawData/traffic_accident_A1/A1_simple/A1_simple.shp")
A2_traffic_accident_simple = gpd.read_file(
    "rawData/traffic_accident_A2/A2_simple/A2_simple.shp")


@app.route('/test')
def index():
    return 'hello! test'


@app.route('/calculate_risk', methods=['POST'])
def calculate_risk():
    print("---------1----------")
    geojson_data = request.json

    polygon_appear = gpd.GeoDataFrame.from_features(geojson_data)
    total_risk = risk_model(
        polygon_appear, A1_traffic_accident_simple, A2_traffic_accident_simple)

    return jsonify({'total_risk': total_risk})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
