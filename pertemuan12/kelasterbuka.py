import os
os.system("cls")

class Item:
    def __init__(self, nama, harga, jumlah = 0):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah
    def hitungHargaTotal(self, jumlah):
        return self.harga * jumlah

brg1 = Item("Buku", 30000, 30)
brg2 = Item("Kursi", 750000, 10)
brg3 = Item("Lampu", 50000, 20)

print("Nama-nama Barang: "+brg1.nama+", "+brg2.nama+", "+brg3.nama)
print("Jumlah Barang "+str(brg1.jumlah+brg2.jumlah+brg3.jumlah)) 
totalHarga = brg1.hitungHargaTotal(brg1.jumlah)+brg2.hitungHargaTotal(brg2.jumlah)+brg3.hitungHargaTotal(brg3.jumlah)
print("Harga Total adalah "+f'{totalHarga:,}')   






# produk1 = Item()

# print("Nama produk ke-1 adalah "+produk1.nama)
# print("Harga satuan produk ke-1 adalah "+f'{produk1.harga:,}')
# print("Harga satuan produk ke-1 adalah "+str(produk1.harga))

# jumlahProduk = 5
# hargaTotal = produk1.hitungHargaTotal(jumlahProduk)

# print("Harga dari "+produk1.nama+" sebanyak " +str(jumlahProduk)+" pcs")
# print("adalah :"+f'{hargaTotal:,}')
# print("adalah :"+str(hargaTotal))




# # print("---------------")
# # produk2 = Item()
# # print("Nama produk ke-2 adalah "+produk2.nama)
# # print("Harga satuan produk ke-2 adalah "+f'{produk2.harga:,}')
