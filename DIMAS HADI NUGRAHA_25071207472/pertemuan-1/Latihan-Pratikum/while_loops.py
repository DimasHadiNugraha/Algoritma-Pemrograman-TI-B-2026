'''while loops pada python'''
#while loops adalah struktur kontrol yang digunakan untuk mengulangi blok kode selama kondisi tertentu bernilai True
#contoh1 sederhana
i = 5 
while i > 0:        #selama nilai i lebih besar dari 0
    print(i)       #tampilkan nilai i
    i -= 1        #kurangi nilai i dengan 1 setiap iterasi

#contoh2 dengan break
j = 1
while j < 10:      #selama nilai j kurang dari 10
    print(j)       #tampilkan nilai j
    if j == 5:     #jika nilai j sama dengan 5
        break      #keluar dari loop
    j += 1         #tambahkan nilai j dengan 1 setiap iterasi

#contoh3 dengan continue
k = 0
while k < 10:      #selama nilai k kurang dari 10
    k += 1         #tambahkan nilai k dengan 1 setiap iterasi
    if k % 2 == 0: #jika nilai k adalah genap
        continue   #lewati iterasi ini
    print(k)       #tampilkan nilai k (hanya ganjil yang ditampilkan)

#contoh4 dengan else
m = 1
while m <= 5:      #selama nilai m kurang dari atau sama dengan 5
    print(m)       #tampilkan nilai m
    m += 1         #tambahkan nilai m dengan 1 setiap iterasi
else:
    print('selesai') #tampilkan pesan 'selesai' setelah loop berakhir
    
