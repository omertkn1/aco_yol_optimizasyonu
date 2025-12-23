
import googlemaps
import numpy as np
import time
import streamlit as st

def get_coordinates(location_name, gmaps_client):
    try:
        res = gmaps_client.geocode(location_name)
        if res:
            loc = res[0]['geometry']['location']
            return loc['lat'], loc['lng']
    except: return None, None
    return None, None

def create_distance_matrix(locations, gmaps_client):
    size = len(locations)
    matrix = np.zeros((size, size))

    prog = st.progress(0)
    status = st.empty()

    for i in range(size):
        status.text(f"Mesafe verisi aliniyor: {i+1}/{size}")
        prog.progress((i + 1) / size)
        try:
            res = gmaps_client.distance_matrix([locations[i]], locations, mode="driving")
            if res['status'] == 'OK':
                elements = res['rows'][0]['elements']
                for j in range(size):
                    if i == j: matrix[i][j] = 0
                    else:
                        if elements[j]['status'] == 'OK':
                            matrix[i][j] = elements[j]['distance']['value']
                        else: matrix[i][j] = 999999
        except: pass
        time.sleep(0.1)

    prog.empty()
    status.empty()
    return matrix

