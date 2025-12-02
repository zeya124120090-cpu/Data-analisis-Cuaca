import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from weather_analyzer import WeatherAnalyzer
from db import dKota as kota

st.set_page_config(page_title="Analisis Data Cuaca Kelompok 6")
st.title("🌤️ Analisis Data Cuaca Kelompok 6")


city = st.selectbox("Pilih Kota:", list(kota.keys()))
lat, lon = kota[city]

# ====================== Fetch API ======================
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={lat}&longitude={lon}&hourly=temperature_2m,relativehumidity_2m"
)
response = requests.get(url).json()
df = pd.DataFrame({
    "time": response["hourly"]["time"],
    "temp": response["hourly"]["temperature_2m"],
    "hum": response["hourly"]["relativehumidity_2m"]
})
df["time"] = pd.to_datetime(df["time"])
st.write("### 🌦️ Data Cuaca")
st.dataframe(df)



# ====================== Analyzer ======================
from weather_analyzer import WeatherAnalyzer
analyzer = WeatherAnalyzer(df["temp"], df["hum"])

col1, col2, col3 = st.columns(3)
col1.metric("Rata-rata Suhu", f"{analyzer.avg_temp():.2f} °C")
col2.metric("Suhu Max", f"{analyzer.max_temp():.2f} °C")
col3.metric("Suhu Min", f"{analyzer.min_temp():.2f} °C")

st.write("### 🌫️ Korelasi Suhu & Kelembapan")
st.write(f"**Pearson Correlation:** {analyzer.correlation():.3f}")



# ====================== GRAFIK ======================
st.write("### 📈 Grafik Suhu 48 Jam")
fig, ax = plt.subplots()
ax.plot(df["time"], df["temp"])
ax.set_xlabel("Waktu")
ax.set_ylabel("Suhu (°C)")
plt.xticks(rotation=45)
st.pyplot(fig)
