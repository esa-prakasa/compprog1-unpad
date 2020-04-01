# Membuat file teks 
f = open("test.txt", "w+") 
for i in range(10):
    s = "Ini baris ke-"+str(i+1)
    f.write(s+"\n")
f.close( )

# Membaca isi file teks
f = open("test.txt", "r")
data = f.read( )
f.close( )
print(data)


