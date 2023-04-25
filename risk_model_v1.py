import pandas as py
import geopandas as gpd
from shapely.geometry import Point
from shapely.ops import cascaded_union
from shapely.geometry import Polygon

def risk_model(polygon_appear,A1_traffic_accident_simple,A2_traffic_accident_simple):
    total_risk = 0

    for index in reversed(polygon_appear.index):
        print(index)

        A1_points_within_polygon = A1_traffic_accident_simple[A1_traffic_accident_simple.geometry.within(polygon_appear.iloc[index].geometry)]
        print(A1_points_within_polygon)
        A1_risk_sum = (A1_points_within_polygon['danger_val'].sum())*0.25

        A2_points_within_polygon = A2_traffic_accident_simple[A2_traffic_accident_simple.geometry.within(polygon_appear.iloc[index].geometry)]
        print(A2_points_within_polygon)
        A2_risk_sum = (A2_points_within_polygon['danger_val'].sum())*0.25

        total_risk += A1_risk_sum + A2_risk_sum
    
    return total_risk