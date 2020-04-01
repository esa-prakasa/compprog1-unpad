# Menambahkan isi file teks 
f = open("test.txt", "a+") 
for i in range(10):
    s = "Penambahan baris ke-"+str(i+1)
    f.write(s+"\n")
f.close( )

# Membaca isi file teks
f = open("test.txt", "r")
data = f.read( )
f.close( )
print(data)


