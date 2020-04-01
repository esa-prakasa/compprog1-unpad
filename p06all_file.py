'''
#===================================#
#     Create File
#===================================#
# Membuat file teks 
f = open("test2.txt", "w+") 
for i in range(10):
    s = "Ini baris ke-"+str(i+1)
    f.write(s+"\n")
f.close( )

# Membaca isi file teks
f = open("test2.txt", "r")
data = f.read( )
f.close( )
print(data)


#===================================#
#   write CSV
#===================================#
#Membuka dan membuat file csv
import csv
with open("provinsi2.csv", mode="a", newline="") as f:
    writer = csv.writer(f, delimiter=",")

    writer.writerow( ["Propinsi", "Ibukota"] )
    writer.writerow( ["Sumatera Utara", "Medan"] )    
    writer.writerow( ["Riau", "Pekanbaru"] )
    writer.writerow( ["Jawa Barat", "Bandung"] )
    writer.writerow( ["Jawa Timur", "Surabaya"] )
    writer.writerow( ["Sulawesi Selatan", "Makasar"] )
    writer.writerow( ["Bali", "Denpasar"])

    writer.writerow( ["Jawa Timur", "Surabaya"])
 
'''  
#===================================#
#   read CSV
#===================================#
#Membaca file csv
import csv
# Membaca data dari file csv
with open("covid30mar.csv", mode="r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        print(row)
