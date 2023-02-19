"""
TUGAS KELOMPOK M04 KOMPUTER GRAFIK

ANGGOTA KELOMPOK: 
- Muhammad Iqbal Fattah (2021071002)
- Ihsan (2021071005)
- Komang Putra Satria Negara (2021071015)
- Anandika Bintang Samudera (2021071018)
- Muhammad Dzakwan Rauhillah (2021071021)
"""

# IMPORT NECESSARY LIBRARIES
import numpy as np
import matplotlib.pyplot as plt

# CREATE A FUNCTION / LIBRARY 

"""
Fungsi untuk membuat titik di 2 dimensi.

Parameter:
y: Koordinat titik pusat sumbu y
x: Koordinat titik pusat sumbu x
pd: Diameter titik
pr: Nilai channel red
pg: Nilai channel green
pb: Nilai channel blue
latar: Kanvas untuk menggambar titik (berupa array 3 dimensi) 
"""
def buat_titik(y, x, pd, pr, pg, pb, latar):
    pic = latar
    r = int(pd / 2)

    for i in range(x - r, x + r + 1):
        for j in range(y - r, y + r + 1):
            if ((i - x) ** 2 + (j - y) ** 2) <= (r ** 2):
                pic[i, j, 0] = pr
                pic[i, j, 1] = pg
                pic[i, j, 2] = pb
    
    return pic

# PREPERATION (Membuat Latar)

row = 500
col = 500

gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)

# USER ENTRIES

print("Program Menggammbar Titik 2 Dimensi")
y = int(input("Masukan nilai y: "))
x = int(input("Masukan nilai x: "))
pd = int(input("Masukan nilai diameter titik: "))
pr = int(input("Masukan nilai channel red: "))
pg = int(input("Masukan nilai channel green: "))
pb = int(input("Masukan nilai channel blue: "))

# MAIN PROGRAM

hasil = buat_titik(y, x, pd, pr, pg, pb, gambar)
plt.imshow(hasil)
plt.show()
