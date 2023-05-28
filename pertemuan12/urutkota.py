import os
os.system("cls")

kota = [[1205,"Banda Aceh"], [879, "Kediri"], 
[907, "Magelang"], [682, "Palembang"],
[1293, "Surabaya"],[750, "Salatiga"]]

N = (len(kota))

print("Sebelum sort")
for i in range(N):
    print(kota[i])

kota.sort()

print("\nSetelah sort")

for i in range(N):
    print(kota[i])

