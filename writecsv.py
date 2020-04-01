#Membuka dan membuat file csv
import csv
with open("test.csv", mode="w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow( ["Propinsi", "Ibukota"] )
    writer.writerow( ["Sumatera Utara", "Medan"] )    
    writer.writerow( ["Riau", "Pekanbaru"] )
    writer.writerow( ["Jawa Barat", "Bandung"] )
    writer.writerow( ["Jawa Timur", "Surabaya"] )
    writer.writerow( ["Sulawesi Selatan", "Makasar"] )
    