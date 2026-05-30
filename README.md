# 📌 Sistem Pendukung Keputusan Penentuan Wilayah Sentra Produksi Tembakau di Kabupaten Jember Menggunakan Metode SAW dan TOPSIS

Repositori ini berisi implementasi **Sistem Pendukung Keputusan (SPK)** untuk menentukan wilayah sentra produksi tembakau di Kabupaten Jember menggunakan kombinasi metode **Simple Additive Weighting (SAW)** dan **Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)**.

---

## 📖 Deskripsi Proyek

Kabupaten Jember merupakan salah satu daerah penghasil tembakau utama di Indonesia dengan persebaran produksi yang berbeda pada setiap kecamatan. Penentuan wilayah sentra produksi tembakau memerlukan analisis berbagai faktor sehingga diperlukan suatu sistem yang mampu membantu proses pengambilan keputusan secara objektif dan berbasis data.

Sistem ini menggunakan pendekatan **Multi-Criteria Decision Making (MCDM)** dengan tahapan:

1. Normalisasi data menggunakan metode **SAW**
2. Perhitungan matriks terbobot
3. Perhitungan solusi ideal positif dan negatif menggunakan **TOPSIS**
4. Perhitungan nilai preferensi dan perangkingan wilayah
5. Menentukan kecamatan yang paling potensial sebagai sentra produksi tembakau

---

## 🎯 Tujuan Sistem

Sistem ini dikembangkan untuk:

* Membantu proses identifikasi wilayah sentra produksi tembakau.
* Menghasilkan perangkingan kecamatan berdasarkan data objektif.
* Mendukung pengambilan keputusan pemerintah daerah dalam pengembangan sektor perkebunan tembakau.
* Mengurangi subjektivitas dalam proses penentuan wilayah sentra produksi.

---

## 📊 Kriteria Penilaian

Sistem menggunakan empat kriteria utama:

| Kode | Kriteria                            | Jenis   |
| ---- | ----------------------------------- | ------- |
| C1   | Total Produksi Tembakau (Ton)       | Benefit |
| C2   | Luas Lahan Perkebunan Tembakau (Ha) | Benefit |
| C3   | Kepadatan Penduduk (Jiwa/Km²)       | Cost    |
| C4   | Jarak ke Ibukota Kabupaten (Km)     | Cost    |

### Bobot Kriteria

| Kriteria | Bobot |
| -------- | ----- |
| C1       | 0.40  |
| C2       | 0.30  |
| C3       | 0.20  |
| C4       | 0.10  |

---

## 📂 Dataset

Dataset penelitian berasal dari publikasi resmi:

**Kabupaten Jember Dalam Angka 2026**
Badan Pusat Statistik (BPS) Kabupaten Jember.

Alternatif yang digunakan adalah kecamatan penghasil tembakau aktif di Kabupaten Jember tahun 2025.

Contoh atribut dataset:

```csv
Kecamatan,Total Produksi,Luas Lahan Perkebunan,Kepadatan Penduduk,Jarak ke Ibukota Kabupaten
Puger,532,380,799.79,29.23
Wuluhan,2050.90,1987,933.53,25.50
Ambulu,926.10,756,1201.49,22.17
```

---

## ⚙️ Metode yang Digunakan

### 1. Simple Additive Weighting (SAW)

Digunakan untuk melakukan normalisasi data berdasarkan jenis kriteria:

**Benefit**

```text
rij = xij / max(xij)
```

**Cost**

```text
rij = min(xij) / xij
```

### 2. TOPSIS

Tahapan perhitungan:

* Normalisasi matriks keputusan
* Matriks ternormalisasi terbobot
* Solusi ideal positif (A⁺)
* Solusi ideal negatif (A⁻)
* Jarak Euclidean (D⁺ dan D⁻)
* Nilai preferensi (Closeness Coefficient)

```text
Pi = D- / (D+ + D-)
```

Nilai preferensi tertinggi menunjukkan wilayah yang paling layak menjadi sentra produksi tembakau.

---

## ⭐ Fitur Sistem

* Upload dataset dalam format CSV
* Perhitungan otomatis metode SAW
* Perhitungan otomatis metode TOPSIS
* Perangkingan kecamatan berdasarkan nilai preferensi
* Tampilan hasil analisis berbasis web
* Antarmuka sederhana dan mudah digunakan

---

## 🛠 Instalasi

Install dependency:

```bash
pip install flask pandas numpy
```

atau

```bash
pip install -r requirements.txt
```

---

## 🚀 Menjalankan Aplikasi

Jalankan aplikasi Flask:

```bash
python appsppk.py
```

Buka browser:

```text
http://127.0.0.1:5000
```

Upload file CSV sesuai format dataset yang telah ditentukan, kemudian sistem akan menampilkan hasil perangkingan wilayah sentra produksi tembakau.

---

## 📁 Struktur Folder

```text
SPK-Sentra-Tembakau/
│
├── appsppk.py
├── requirements.txt
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── dataset/
│   └── tembakau_jember.csv
│
└── README.md
```

---

## 📚 Referensi

* Afshari, A., Mojahed, M., & Yusuff, R. M. (2020). *Simple Additive Weighting Approach*.
* Behzadian, M., et al. (2022). *A State-of-the-Art Survey of TOPSIS Applications*.
* Velasquez, M., & Hester, P. T. (2021). *An Analysis of Multi-Criteria Decision Making Methods*.
* Badan Pusat Statistik Kabupaten Jember. (2026). *Kabupaten Jember Dalam Angka 2026*.

---

## 📄 Lisensi

Proyek ini dikembangkan untuk keperluan akademik dan penelitian pada Program Studi Sistem Informasi Fakultas Ilmu Komputer Universitas Jember. Penggunaan untuk tujuan pendidikan dan penelitian diperbolehkan dengan tetap mencantumkan sumber yang sesuai.
