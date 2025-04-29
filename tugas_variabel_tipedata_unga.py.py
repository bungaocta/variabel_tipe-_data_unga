
# =============================
# 1. Jenis-jenis Tipe Data di Python
# =============================

# Integer (bilangan bulat)
angka = 10

# Float (bilangan desimal)
desimal = 3.14

# String (teks)
nama = "Muchtar Ali"

# Boolean (True/False)
is_siswa = True

# List (daftar)
hobi = ["membaca", "ngoding", "olahraga"]

# Tuple (mirip list tapi tidak bisa diubah)
koordinat = (10, 20)

# Dictionary (pasangan key dan value)
biodata = {"nama": "Ali", "umur": 20}

# Set (kumpulan data unik)
angka_unik = {1, 2, 3, 3, 2}

# =============================
# 2. Program Biodata dengan Komentar
# =============================

# Nama : Muchtar Ali Setyo Yudono
# Nomor Telepon : 0426019502
# NIM : 089677568788

print("\n===== Soal 2: Biodata =====")
print("Muchtar Ali Setyo Yudono")
print("0426019502")
print("089677568788")

# =============================
# 3. Operasi Aritmatika dari Tiga Angka
# =============================
print("\n===== Soal 3: Operasi Aritmatika =====")

angka1 = 5000
angka2 = 2000
angka3 = 200

angka1 += 500
angka2 += 500

hasil1 = angka1 + angka2
hasil2 = angka2 - angka3

print("Hasil Penjumlahan: ", hasil1)
print("Hasil Pengurangan: ", hasil2)

# =============================
# 4. Keliling Lingkaran dan Volume Kubus
# =============================
import math

print("\n===== Soal 4: Keliling Lingkaran dan Volume Kubus =====")
r = float(input("Masukkan jari-jari lingkaran: "))
keliling = 2 * math.pi * r
print("Keliling lingkaran: {:.2f}".format(keliling))

sisi = float(input("Masukkan panjang sisi kubus: "))
volume = sisi ** 3
print("Volume kubus: {:.2f}".format(volume))
