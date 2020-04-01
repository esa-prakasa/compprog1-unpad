import csv
# Membaca data dari file csv
with open("covid30mar.csv", mode="r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        print(row)