# car-accident-risk-model
This repository contains the source code for a risk calculation program developed by NTU DAC in collaboration with Gogoro Inc. as part of a joint project. Due to commercial sensitivity, only the part using publicly available datasets is released.

The program includes a Flask-based API that calculates the risk of traffic accidents based on publicly available data. Given a user-defined GeoJSON of their living area, the program calculates the risk of traffic accidents in Taiwan over the past few years and provides a risk value based on proportions.

## Getting Started
### Prerequisites
To run the program, you will need Python 3.7 or higher and the following packages:

- Flask
- pandas
- numpy
- shapely
- geopandas

## Running the Program
All materials you need can be found in file: rawData and Flask-API-Risk-modelV1

To start the program, run the following command:
```
python3 run.py
```

This will start the Flask server and make the API available at http://localhost:3000.

## Usage
- rawData: This folder contains the raw data required for the program to run.
- Flask-API-Risk-modelV1: This folder contains the source code of the program.
- data-preprocessing: This folder contains the Python code for processing Taiwan A1 A2 car accident open data to create the rawData folder.
- risk_model_v1.ipynb: This Jupyter notebook contains the visualization results presented by folium.

## Using the API
To use the API, send a POST request to the endpoint /calculate_risk with a GeoJSON of the user's living area in the request body. The program will calculate the risk of traffic accidents in the user's living area based on publicly available data and return a risk value in the response.

You can use testingGeojson.geojson to test this API
The response will be a risk value for the user's living area.

You can use Postman to test this API:
1. Open your Postman 
2. Use http://localhost:3000 for testing
3. Choose Post
4. Paste the code from `testingGeojson.geojson` on Postman
5. This API will return a danger value of these areas

## License
This program is licensed under the MIT License - see the LICENSE file for details.
