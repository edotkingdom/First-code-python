# Bentuk For

jumlah_buku = 10
print("Baca Semua buku")
jumlah_buku_telah_dibaca = 0
print(f"jumlah buku yang dibaca adalah {jumlah_buku_telah_dibaca}")

for jumlah_buku_telah_dibaca in range(1,jumlah_buku+1):
    print(f"buku ke -{jumlah_buku_telah_dibaca}")

# Bentuk While
print("+++Bentuk while++++")
jumlah_buku_while = 100
jumlah_buku_telah_dibaca_while =0
while jumlah_buku_telah_dibaca_while < jumlah_buku_while:
    jumlah_buku_telah_dibaca_while = jumlah_buku_telah_dibaca_while+1
    print(f"jumlah buku yang telah dibaca {jumlah_buku_telah_dibaca_while}")

print(f"jumlah buku yang telah dibaca{jumlah_buku_telah_dibaca_while}")