from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

# Bobot kriteria
bobot = {
    "Total Produksi": 0.40,
    "Luas Lahan Perkebunan": 0.30,
    "Kepadatan Penduduk": 0.20,
    "Jarak ke Ibukota Kabupaten": 0.10
}

# Jenis kriteria
jenis_kriteria = {
    "Total Produksi": "benefit",
    "Luas Lahan Perkebunan": "benefit",
    "Kepadatan Penduduk": "cost",
    "Jarak ke Ibukota Kabupaten": "cost"
}


def bersihkan_angka(nilai):
    if isinstance(nilai, str):
        nilai = nilai.replace(".", "").replace(",", ".")
    return float(nilai)


def hitung_saw(df):
    data = df.copy()
    kriteria = list(bobot.keys())

    X = data[kriteria].applymap(bersihkan_angka)

    normalisasi = pd.DataFrame()
    for k in kriteria:
        if jenis_kriteria[k] == "benefit":
            normalisasi[k] = X[k] / X[k].max()
        else:
            normalisasi[k] = X[k].min() / X[k]

    nilai_saw = sum(normalisasi[k] * bobot[k] for k in kriteria)

    hasil = pd.DataFrame()
    hasil["Kecamatan"] = data["Kecamatan"]
    hasil["Nilai SAW"] = nilai_saw
    hasil["Ranking"] = hasil["Nilai SAW"].rank(ascending=False, method="min").astype(int)
    hasil = hasil.sort_values("Ranking")

    return hasil


def hitung_topsis(df):
    data = df.copy()
    kriteria = list(bobot.keys())

    X = data[kriteria].applymap(bersihkan_angka).values
    W = np.array([bobot[k] for k in kriteria])

    # Normalisasi matriks TOPSIS
    normalisasi = X / np.sqrt((X ** 2).sum(axis=0))

    # Matriks terbobot
    terbobot = normalisasi * W

    # Solusi ideal positif dan negatif
    ideal_pos = []
    ideal_neg = []

    for i, k in enumerate(kriteria):
        if jenis_kriteria[k] == "benefit":
            ideal_pos.append(terbobot[:, i].max())
            ideal_neg.append(terbobot[:, i].min())
        else:
            ideal_pos.append(terbobot[:, i].min())
            ideal_neg.append(terbobot[:, i].max())

    ideal_pos = np.array(ideal_pos)
    ideal_neg = np.array(ideal_neg)

    # Jarak solusi Euclidean
    d_pos = np.sqrt(((terbobot - ideal_pos) ** 2).sum(axis=1))
    d_neg = np.sqrt(((terbobot - ideal_neg) ** 2).sum(axis=1))

    # Nilai preferensi TOPSIS
    nilai_topsis = d_neg / (d_pos + d_neg)

    hasil = pd.DataFrame()
    hasil["Kecamatan"] = data["Kecamatan"]
    hasil["D+"] = d_pos
    hasil["D-"] = d_neg
    hasil["Nilai TOPSIS"] = nilai_topsis
    hasil["Ranking"] = hasil["Nilai TOPSIS"].rank(ascending=False, method="min").astype(int)
    hasil = hasil.sort_values("Ranking")

    return hasil


@app.route("/", methods=["GET", "POST"])
def index():
    hasil_saw = None
    hasil_topsis = None
    error_message = None

    if request.method == "POST":
        file = request.files.get("file")

        if not file or file.filename == "":
            error_message = "File CSV belum dipilih."
        else:
            try:
                df = pd.read_csv(file, sep=",", engine="python")
                df.columns = df.columns.str.strip()

                # Jika header masih terbaca sebagai satu kolom, coba baca ulang dengan delimiter ;
                if len(df.columns) == 1 or "Kecamatan" not in df.columns:
                    file.seek(0)
                    df = pd.read_csv(file, sep=";", engine="python")
                    df.columns = df.columns.str.strip()

                # Jika masih gagal, tampilkan nama kolom
                print(df.columns.tolist())

                kolom_wajib = ["Kecamatan"] + list(bobot.keys())

                for kolom in kolom_wajib:
                    if kolom not in df.columns:
                        error_message = f'Kolom "{kolom}" tidak ditemukan pada file CSV.'
                        break

                if error_message is None:
                    hasil_saw_df = hitung_saw(df)
                    hasil_topsis_df = hitung_topsis(df)

                    hasil_saw = hasil_saw_df.to_html(
                        index=False,
                        classes="table table-striped",
                        float_format=lambda x: f"{x:.3f}"
                    )

                    hasil_topsis = hasil_topsis_df.to_html(
                        index=False,
                        classes="table table-striped",
                        float_format=lambda x: f"{x:.3f}"
                    )

            except Exception as e:
                error_message = f"Gagal memproses file: {str(e)}"

    return render_template(
        "index.html",
        hasil_saw=hasil_saw,
        hasil_topsis=hasil_topsis,
        error_message=error_message
    )


if __name__ == "__main__":
    app.run(debug=True)