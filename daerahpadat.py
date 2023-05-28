import os
os.system("cls")

kepadatan_penduduk = [1500, 1001, 1500, 1800, 2000, 400, 700, 1230,
600, 7000, 1000, 345, 7800]

# Penentuan daerah padat penduduk
daerah_padat = []

for kepadatan in kepadatan_penduduk:
    if kepadatan > 2000:
        daerah_padat.append(True)
    else:
        daerah_padat.append(False)

# Menampilkan hasil penentuan kepadatan
for i in range(len(kepadatan_penduduk)):
    area = "Daerah " + str(i+1) + " kepadatan "+f'{kepadatan_penduduk[i]:,}'
    if daerah_padat[i]:
        print(area, ": Terlalu padat.")
    else:
        print(area, ": Normal.")




