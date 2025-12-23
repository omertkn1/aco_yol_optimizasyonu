
import streamlit as st
import googlemaps
import folium
from streamlit_folium import st_folium
import numpy as np
import pickle
import os
import time
import pandas as pd

from data.coordinates import SCHOOLS
from core.matrix_utils import get_coordinates, create_distance_matrix
from core.ant_algorithm import AntColonyOptimization

st.set_page_config(layout="wide", page_title="Bursa ACO")
st.title("Bursa Geri Donusum Rota Optimizasyonu")

SAVE_FILE = "sonuclar.pkl"

st.sidebar.header("Ayarlar")

# API Anahtari Yonetimi
default_api_key = ""
try:
    if "google_maps_api_key" in st.secrets:
        default_api_key = st.secrets["google_maps_api_key"]
except: pass

api_key = st.sidebar.text_input("Google Maps API Key", value=default_api_key, type="password")

n_ants = st.sidebar.slider("Karinca Sayisi", 10, 200, 50)
n_iter = st.sidebar.slider("Iterasyon", 10, 500, 100)
decay = st.sidebar.slider("Decay", 0.0, 1.0, 0.95)
alpha = st.sidebar.slider("Alpha", 0.0, 5.0, 1.0)
beta = st.sidebar.slider("Beta", 0.0, 5.0, 2.0)

if st.sidebar.button("ROTAYI HESAPLA"):
    if not api_key:
        st.error("Lutfen once API Anahtarini girin!")
        st.stop()

    try:
        gmaps = googlemaps.Client(key=api_key)
    except:
        st.error("API Anahtari gecersiz.")
        st.stop()

    lats, valid_idx = [], []
    with st.spinner("Harita verileri aliniyor..."):
        for i, s in enumerate(SCHOOLS):
            lt, ln = get_coordinates(s, gmaps)
            if lt: lats.append((lt, ln)); valid_idx.append(i)

        if len(lats) < 2: st.error("Yeterli veri yok."); st.stop()
        matrix = create_distance_matrix([SCHOOLS[i] for i in valid_idx], gmaps)

    with st.spinner("Rota optimize ediliyor..."):
        aco = AntColonyOptimization(matrix, n_ants, int(n_ants/2), n_iter, decay, alpha, beta)
        path, dist, history = aco.run()

    data = {"dist": dist, "path": path, "history": history, "lats": lats, "valid_idx": valid_idx}
    with open(SAVE_FILE, "wb") as f: pickle.dump(data, f)

    st.success("Bitti!")
    time.sleep(0.5)
    st.rerun()

if os.path.exists(SAVE_FILE):
    try:
        with open(SAVE_FILE, "rb") as f: res = pickle.load(f)
        c1, c2 = st.columns([2, 1])
        with c1:
            st.info(f"Mesafe: {int(res['dist'])} metre")
            m = folium.Map(location=[res['lats'][0][0], res['lats'][0][1]], zoom_start=12)

            folium.PolyLine([res['lats'][i] for i in res['path']], color="red", weight=4).add_to(m)

            for i, idx in enumerate(res['path']):
                folium.Marker(res['lats'][idx], tooltip=f"{i}. Durak").add_to(m)

            st_folium(m, width=700)

        with c2:
            st.write("### Yakinsama Grafigi")
            chart_data = pd.DataFrame(res['history'], columns=["Mesafe"])
            st.line_chart(chart_data)

            st.write("### Ziyaret Sirasi")
            for i, idx in enumerate(res['path']):
                st.write(f"**{i}.** {SCHOOLS[res['valid_idx'][idx]]}")

        if st.sidebar.button("Temizle"):
            os.remove(SAVE_FILE)
            st.rerun()
    except Exception as e:
        st.error(f"Hata: {e}")
