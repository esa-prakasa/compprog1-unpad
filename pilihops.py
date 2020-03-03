x = float(input('Masukkan sebuah bilangan integer pertama: '))
y = float(input('Masukkan sebuah bilangan integer kedua: '))


print ('1) Penjumlahan dua bilangan')
print ('2) Pengurangan dua bilangan')
print ('3) Perkalian dua bilangan')
print ('4) Pembagian dua bilangan')

pilihan = int(input('Silahkan masukkan kode pilihan operasi matematika '))

print('Jawaban hasil operasi '+str(x)+' dan '+str(y))

if pilihan ==1:
    print(x+y)
elif pilihan ==2:
    print(x-y)
elif pilihan ==3:
    print(x*y)
elif pilihan ==4:
    print(x/y)
else:
    print('Kode pilihan operasi tidak sesuai')

        
