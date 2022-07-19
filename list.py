buku = ['jejak si gundul','kabayan ke jawa','kunaon es']
print(buku)

for i in range(0,len(buku)):
    print(buku[i])


buku.append('kiwari')
print(buku)

for i in range(0,len(buku)):
    print(buku[i])


print("\nTampilkan Proses Semua Buku")
for books in buku:
    print(books)
