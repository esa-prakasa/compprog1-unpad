import os
os.system("cls")

class MenuItem:
    def __init__(self, nama, deskripsi, harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.tersedia = True

# Buat beberapa menu
item1 = MenuItem("Ayam Goreng", "Nasi dan sambal", 15000)
item2 = MenuItem("Bakso", "Mie dan pangsit", 20000)
item3 = MenuItem("Gulai Sapi", "Nasi dan Es Teh ", 30000)

# Buat List yang menyimpan semua pilihan menu
daftar_menu = [item1, item2, item3]

# Menampilkan semua menu yang tersedia
print("===================================")
print("\nPilihan Menu yang tersedia semula\n")
idx = 1
for item in daftar_menu:
    print("Menu No "+str(idx))
    idx+=1
    print("Nama:", item.nama)
    print("Tambahan:", item.deskripsi)
    print("Harga: Rp.", f'{item.harga:,}')
    print("Tersedia:", "Ada" if item.tersedia else "Habis")
    print()

item1.tersedia = False
item2.tersedia = False

# Tambahan menu baru
item4 = MenuItem("Nasi Goreng", "Sosis dan kerupuk ", 10000)
daftar_menu.append(item4)

item5 = MenuItem("Nasi Uduk", "Telur", 8000)
daftar_menu.append(item5)

item6 = MenuItem("Bubur Ayam", "Kerupuk", 7000)
daftar_menu.append(item6)

item1.tersedia = True

print("Pilihan Menu yang tersedia saat ini\n")

idx = 1
for item in daftar_menu:
    if item.tersedia == True:
        print("Menu No "+str(idx))
        idx+=1
        print("Nama:", item.nama)
        print("Tambahan:", item.deskripsi)
        print("Harga: Rp.", f'{item.harga:,}')
        print("Tersedia:", "Ada" if item.tersedia else "Habis")
        print()

