# Menyimpan sebuah variabel Dictionary dalam sebuah variabel
# Dictionary yang lain
data = {
    "location": "Pantai Pangandaran",
    "visitors": { "2018": 200, "2017": 150 }
}
# Menampilkan output berupa data dengan key wins
print( data["visitors"] ) 

# Menampilkan output berupa data dengan key wins dan tahun
print( data["visitors"]["2018"] )