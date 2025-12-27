import pandas as pd


# NO 1
# Membuat DataFrame dari data produksi sampah

df = pd.read_csv("static/download/sampah.csv")

# Menyesuaikan nama kolom sesuai ketentuan soal
df = df.rename(columns={
    "nama_kabupaten_kota": "Kabupaten_Kota",
    "jumlah_sampah": "Jumlah_Sampah_Ton",
    "tahun": "Tahun"
})

# Mengambil kolom yang dibutuhkan saja
df = df[["Kabupaten_Kota", "Jumlah_Sampah_Ton", "Tahun"]]

print("DataFrame Produksi Sampah Jawa Barat")
print(df.head())


#  NO 2
# Total produksi sampah untuk tahun tertentu
# (WAJIB menggunakan iterrows)

tahun_dicari = 2020
total_sampah_tahun = 0

for index, row in df.iterrows():
    if row["Tahun"] == tahun_dicari:
        total_sampah_tahun += row["Jumlah_Sampah_Ton"]

print(f"\nTotal produksi sampah Jawa Barat tahun {tahun_dicari}:")
print(total_sampah_tahun, "ton")

#  NO 3
# Jumlahkan data per tahun

total_per_tahun = {}

for index, row in df.iterrows():
    tahun = row["Tahun"]
    jumlah = row["Jumlah_Sampah_Ton"]

    if tahun not in total_per_tahun:
        total_per_tahun[tahun] = 0

    total_per_tahun[tahun] += jumlah

df_total_tahun = pd.DataFrame(
    total_per_tahun.items(),
    columns=["Tahun", "Total_Sampah_Ton"]
)

print("\nTotal Produksi Sampah per Tahun")
print(df_total_tahun)


#  NO 4
# Jumlahkan data per Kabupaten/Kota per tahun
# (WAJIB menggunakan iterrows)

total_kab_kota = {}

for index, row in df.iterrows():
    key = (row["Kabupaten_Kota"], row["Tahun"])

    if key not in total_kab_kota:
        total_kab_kota[key] = 0

    total_kab_kota[key] += row["Jumlah_Sampah_Ton"]

df_kab_kota = pd.DataFrame(
    [(k[0], k[1], v) for k, v in total_kab_kota.items()],
    columns=["Kabupaten_Kota", "Tahun", "Total_Sampah_Ton"]
)

print("\nTotal Produksi Sampah per Kabupaten/Kota per Tahun")
print(df_kab_kota.head())

# EXPORT HASIL AKHIR KE CSV DAN EXCEL

df.to_csv("static/download/data_sampah_jabar.csv", index=False)
df.to_excel("static/download/data_sampah_jabar.xlsx", index=False)

df_total_tahun.to_csv("static/download/total_sampah_per_tahun.csv", index=False)
df_total_tahun.to_excel("static/download/total_sampah_per_tahun.xlsx", index=False)

df_kab_kota.to_csv("static/download/total_sampah_kab_kota_per_tahun.csv", index=False)
df_kab_kota.to_excel("static/download/total_sampah_kab_kota_per_tahun.xlsx", index=False)

print("\nSemua file berhasil diexport")
