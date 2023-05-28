import os
os.system("cls")

class Item:
    nama = "Baju"
    harga = 300000
    def hitungHargaTotal(self, jumlah):
        return self.harga * jumlah

produk1 = Item()

print("Nama produk ke-1 adalah "+produk1.nama)
print("Harga satuan produk ke-1 adalah "+f'{produk1.harga:,}')
print("Harga satuan produk ke-1 adalah "+str(produk1.harga))

jumlahProduk = 5
hargaTotal = produk1.hitungHargaTotal(jumlahProduk)

print("Harga dari "+produk1.nama+" sebanyak " +str(jumlahProduk)+" pcs")
print("adalah :"+f'{hargaTotal:,}')
print("adalah :"+str(hargaTotal))




# print("---------------")
# produk2 = Item()
# print("Nama produk ke-2 adalah "+produk2.nama)
# print("Harga satuan produk ke-2 adalah "+f'{produk2.harga:,}')
