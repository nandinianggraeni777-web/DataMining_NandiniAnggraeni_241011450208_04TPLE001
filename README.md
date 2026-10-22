# Data Mining

Proyek ini berisi dua contoh analisis data menggunakan Python, yaitu analisis dataset penerbangan dan analisis dataset Iris. Struktur proyek mengikuti folder `data mining` pada screenshot.

## Struktur Folder

```text
data mining/
├── venv/
├── .gitignore
├── Data_Penerbangan.py
├── dataset_penerbangan_1500.csv
├── Iris.csv
├── requirements.txt
└── tugas.py
```

Keterangan:
- `Data_Penerbangan.py` — skrip untuk eksplorasi dan analisis dataset penerbangan.
- `dataset_penerbangan_1500.csv` — dataset penerbangan berisi 1.500 baris data, sesuai nama file. Jumlah aktual dapat diperiksa saat program dijalankan.
- `Iris.csv` — dataset bunga Iris.
- `tugas.py` — skrip analisis dataset Iris.
- `requirements.txt` — daftar pustaka Python yang diperlukan.
- `venv/` — lingkungan virtual Python lokal. Umumnya folder ini tidak perlu dimasukkan ke repositori Git.

## 1. Analisis Dataset Penerbangan

Skrip `Data_Penerbangan.py` membaca file `dataset_penerbangan_1500.csv` yang berada di folder yang sama dengan skrip.

### Analisis yang dilakukan
- Memuat dataset menggunakan Pandas.
- Mengubah kolom tanggal dan waktu menjadi tipe `datetime`.
- Mengidentifikasi kolom numerik dan kategorikal.
- Menampilkan jumlah baris dan kolom.
- Memeriksa jumlah data duplikat dan nilai kosong (`null`).
- Menghitung jumlah nilai nol pada kolom numerik.
- Membagi fitur (`X`) dan target (`y`), dengan target `status_penerbangan`.
- Membagi data menjadi 80% data latih dan 20% data uji menggunakan `train_test_split`.
- Membuat diagram batang jumlah penerbangan berdasarkan status.

### Menjalankan analisis penerbangan

Pastikan terminal berada di folder proyek, lalu jalankan:

```bash
python Data_Penerbangan.py
```

Skrip menggunakan lokasi file yang dibangun berdasarkan lokasi skrip, sehingga file CSV dapat dibaca selama berada di folder yang sama.

## 2. Analisis Dataset Iris

Skrip `tugas.py` digunakan untuk mengeksplorasi dataset bunga Iris dari file `Iris.csv`.

### Analisis yang dilakukan
- Menampilkan lima baris pertama.
- Menampilkan ukuran dan informasi dataset.
- Memeriksa data kosong dan duplikat.
- Menampilkan statistik deskriptif.
- Menghitung jumlah data berdasarkan `Species`.
- Menghitung rata-rata `PetalLengthCm`.
- Membuat diagram batang jumlah setiap spesies Iris.
- Membuat scatter plot hubungan `PetalLengthCm` dan `PetalWidthCm` untuk setiap spesies.

### Menjalankan analisis Iris

```bash
python tugas.py
```

Pastikan `Iris.csv` tersedia di folder yang sama dengan file Python. Pada skrip Iris, nama file yang dibaca adalah `Iris.csv` (huruf besar-kecil harus sesuai dengan nama file di sistem yang digunakan).

## Persyaratan

Gunakan Python 3 dan pustaka berikut:
- `pandas`
- `numpy`
- `matplotlib`
- `scikit-learn`

Instal dependensi dengan:

```bash
pip install -r requirements.txt
```

Jika `requirements.txt` belum berisi dependensi tersebut, isi dengan:

```text
pandas
numpy
matplotlib
scikit-learn
```

## Catatan Penting

1. Potongan kode yang diberikan mencampurkan kode analisis penerbangan dan Iris. Agar masing-masing skrip dapat dijalankan tanpa error, pisahkan kode penerbangan ke `Data_Penerbangan.py` dan kode Iris ke `tugas.py`.
2. Kode penerbangan menggunakan kolom `status_penerbangan`. Pastikan kolom tersebut memang tersedia pada CSV.
3. Kode Iris menggunakan kolom `Species`, `PetalLengthCm`, dan `PetalWidthCm`. Pastikan nama kolom di `Iris.csv` cocok.
4. Pada skrip penerbangan, `train_test_split` membagi data, tetapi belum melatih model machine learning. Bagian tersebut baru menyiapkan data untuk tahap pemodelan berikutnya.
5. `LabelEncoder` pada kode Iris diimpor tetapi tidak digunakan, sehingga baris impor tersebut boleh dihapus jika tidak diperlukan.
6. Sebaiknya folder `venv/` tidak diunggah ke Git. Tambahkan `venv/` ke `.gitignore` jika belum ada.

## Tujuan Proyek

Proyek ini merupakan latihan eksplorasi data (*Exploratory Data Analysis/EDA*) dan persiapan awal machine learning pada dua jenis dataset: penerbangan dan bunga Iris.
