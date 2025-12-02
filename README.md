#  **Aplikasi Analisis Data Cuaca – Kelompok 6**

Sumber Data: **Open-Meteo API (Gratis & Real-Time)**
Website API: [https://open-meteo.com/](https://open-meteo.com/)

---

##  **Deskripsi Proyek**

Aplikasi ini merupakan **program analisis data cuaca** yang datanya diambil secara real-time dari **Open-Meteo API**, sebuah layanan cuaca gratis tanpa API key. Aplikasi dibangun menggunakan **Python**, menerapkan **Object-Oriented Programming (OOP)** serta berbagai library seperti **NumPy, SciPy, Matplotlib**, dan antarmuka GUI menggunakan **Streamlit**.

Pengguna dapat memilih kota, mengambil data cuaca terbaru, melihat tabel data, melakukan analisis statistik, hingga menampilkan grafik suhu.

---

##  **Tujuan Proyek**

1. Mengambil data cuaca **secara real-time** dari Open-Meteo.
2. Melakukan **analisis statistik suhu dan kelembapan**, seperti:
   * Rata-rata suhu
   * Suhu tertinggi
   * Suhu terendah
   * Korelasi suhu dan kelembapan
3. Membuat **aplikasi interaktif** menggunakan Streamlit.
4. Mengimplementasikan **OOP** dalam pengolahan data cuaca.

---

##  **Data Sumber**

Semua data diambil secara langsung dari:

> **Open-Meteo Weather API**
> [https://open-meteo.com/](https://open-meteo.com/)

API ini **gratis sepenuhnya**, tidak membutuhkan API key, dan menyediakan data cuaca seperti:

* Suhu (temperature_2m)
* Kelembapan (relativehumidity_2m)
* Angin
* Curah hujan
* dan lainnya

Contoh request:

```
https://api.open-meteo.com/v1/forecast?latitude=-5.45&longitude=105.27&hourly=temperature_2m,relativehumidity_2m
```
