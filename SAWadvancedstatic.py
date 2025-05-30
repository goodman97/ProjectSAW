import streamlit as st
import pandas as pd
import numpy as np

st.title("SAW - Rekomendasi Tempat Wisata (Statis)")
st.text("Oleh: Martin Aji Nugraha / 123230092 / IF-B")

# Load data dari file lokal
st.header("Data Tempat Wisata")
df = pd.read_csv("tourism_dataset_5000.csv")
st.dataframe(df)

# Ambil kolom kriteria
kriteria_df = df[['Site Name', 'Tourist Rating', 'System Response Time',
                  'Recommendation Accuracy', 'VR Experience Quality', 'Satisfaction']]

# Group by site (karena bisa duplikat tiap pengunjung)
kriteria_df = kriteria_df.groupby('Site Name').mean().reset_index()

# Definisikan cost(0)/benefit(1)
cb = [1, 0, 1, 1, 1]

# Bobot tiap kriteria (total 1)
w = [0.25, 0.2, 0.2, 0.2, 0.15]

# Matriks keputusan
x = kriteria_df.drop(columns=['Site Name']).values

# Normalisasi matriks
R = np.zeros_like(x, dtype=float)
for j in range(len(cb)):
    if cb[j] == 1:
        R[:, j] = x[:, j] / x[:, j].max()
    else:
        R[:, j] = x[:, j].min() / x[:, j]

# Hitung nilai akhir SAW
V = np.dot(R, w)

# Buat hasil dataframe
hasil = pd.DataFrame({
    'Site Name': kriteria_df['Site Name'],
    'SAW Score': V
})

# Urutkan hasil
hasil_sorted = hasil.sort_values(by='SAW Score', ascending=False).reset_index(drop=True)

st.header("Hasil SAW Score")
st.dataframe(hasil)

st.header("Ranking Tempat Wisata")
st.dataframe(hasil_sorted)

