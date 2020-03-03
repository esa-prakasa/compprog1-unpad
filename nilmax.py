x = int(input('Masukkan sebuah bilangan integer pertama: '))
y = int(input('Masukkan sebuah bilangan integer kedua: '))
z = int(input('Masukkan sebuah bilangan integer ketiga: '))

if (y>x):
    if (z>y):
        nMax = z        
    else:
        nMax = y
else:
    if (z>x):
        nMax = z
    else:
        nMax = x

print('Nilai terbesar dari '+str(x)+', '+str(y)+' dan '+str(z)+' adalah: '+str(nMax))


