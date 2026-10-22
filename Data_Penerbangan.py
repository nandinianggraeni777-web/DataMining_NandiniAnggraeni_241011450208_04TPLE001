from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


# Memuat dataset dari folder yang sama dengan file Python ini.
path_dataset = Path(__file__).resolve().parent / "dataset_penerbangan_1500.csv"
df = pd.read_csv(path_dataset)

# Ubah kolom tanggal/waktu dari teks menjadi tipe datetime.
kolom_datetime = [
	"tanggal_penerbangan",
	"jadwal_keberangkatan",
	"aktual_keberangkatan",
	"jadwal_kedatangan",
	"aktual_kedatangan",
]
for kolom in kolom_datetime:
	df[kolom] = pd.to_datetime(df[kolom], errors="coerce")

kolom_numerik = sorted(df.select_dtypes(include=np.number).columns.tolist())
kolom_kategorikal = sorted(
	kolom
	for kolom in df.columns
	if kolom not in kolom_datetime and not pd.api.types.is_numeric_dtype(df[kolom])
)

print("=== INFORMASI DATASET ===")
print(f"Lokasi dataset: {path_dataset}")
print(f"Jumlah baris: {df.shape[0]}")
print(f"Jumlah kolom: {df.shape[1]}")

print("\n=== KOLOM KATEGORIKAL ===")
print(f"Jumlah kolom kategorikal: {len(kolom_kategorikal)}")
print(kolom_kategorikal)

print("\n=== KOLOM NUMERIKAL ===")
print(f"Jumlah kolom numerikal: {len(kolom_numerik)}")
print(kolom_numerik)

print("\n=== KOLOM TANGGAL/WAKTU ===")
print(f"Jumlah kolom tanggal/waktu: {len(kolom_datetime)}")
print(sorted(kolom_datetime))

print("\n=== DATA DUPLIKAT ===")
print(f"Jumlah baris duplikat: {df.duplicated().sum()}")

jumlah_null = df.isna().sum().sort_values(ascending=False)
print("\n=== DATA NULL PER KOLOM ===")
print(jumlah_null[jumlah_null > 0])
print(f"Jumlah seluruh nilai null: {jumlah_null.sum()}")

jumlah_zero = pd.Series(
	np.count_nonzero(df[kolom_numerik].to_numpy() == 0, axis=0),
	index=kolom_numerik,
).sort_index()
print("\n=== DATA ZERO PER KOLOM NUMERIK ===")
print(jumlah_zero)
print(f"Jumlah seluruh nilai zero: {jumlah_zero.sum()}")

# Bagi fitur dan target untuk persiapan analisis machine learning.
X = df.drop(columns="status_penerbangan")
y = df["status_penerbangan"]
X_train, X_test, y_train, y_test = train_test_split(
	X, y, test_size=0.2, random_state=42
)
print("\n=== PEMBAGIAN DATA (SCIKIT-LEARN) ===")
print(f"Jumlah data latih: {len(X_train)}")
print(f"Jumlah data uji: {len(X_test)}")

# Visualisasi jumlah penerbangan pada setiap status.
jumlah_status = df["status_penerbangan"].value_counts().sort_index()
plt.figure(figsize=(8, 5))
plt.bar(jumlah_status.index, jumlah_status.values, color="steelblue")
plt.title("Jumlah Penerbangan Berdasarkan Status")
plt.xlabel("Status Penerbangan")
plt.ylabel("Jumlah")
plt.tight_layout()
plt.show()
