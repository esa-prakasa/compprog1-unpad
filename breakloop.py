A = [10, 20, 30, 40, 50]
N = len(A)
print('Jumlah elemen: '+str(N))
idx = int(input('Indeks yang dilewati? [0 ~ 4] '))

for i in range(N):
    if i == idx:
        break
    print('Data ke-'+str(i)+': '+str(A[i]))
