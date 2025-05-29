import streamlit as st
import pandas as pd
import numpy as np

st.title('SAW Pemilihan Tempat Wisata')
st.text('Martin Aji Nugraha / 123230092 / IF-B')
st.text('Faisal Dani Noto Legowo / 123230097 / IF-B')

# Load data
st.header('Load Data File .csv')
df = pd.read_csv("tourism_dataset_5000.csv")
st.dataframe(df)

# Alternatif (Site Name)
alter = df['Site Name'].tolist()

# Matriks keputusan (Tourist Rating, System Response Time, Recommendation Accuracy, VR Experience Quality, Satisfaction)
kriteria = ['Tourist Rating', 'System Response Time', 'Recommendation Accuracy', 'VR Experience Quality', 'Satisfaction']
x = df[kriteria].values

# cost(0) / benefit(1)
cb = [1, 0, 1, 1, 1]

# Bobot tiap kriteria
w = [4, 3, 5, 4, 3]

# Normalisasi matriks
R = np.zeros_like(x, dtype=float)

for j in range(len(cb)):
    if cb[j] == 1:
        R[:, j] = x[:, j] / x[:, j].max()  # benefit
    else:
        R[:, j] = x[:, j].min() / x[:, j]  # cost

# Perhitungan nilai akhir SAW
V = np.dot(R, w)

# Hasil dataframe
hasil = pd.DataFrame({
    'Tempat Wisata': alter,
    'Skor SAW': V
})

# Urutkan hasil
hasilsort = hasil.sort_values(by='Skor SAW', ascending=False)

# Tampilkan hasil
st.header('Hasil Ranking SAW')
st.text('Hasil Skor')
st.dataframe(hasil)

st.text('Hasil Yang Diurutkan dari Nilai Terbesar')
st.dataframe(hasilsort)
