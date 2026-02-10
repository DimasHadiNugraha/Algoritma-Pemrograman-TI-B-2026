'''python for loops'''
    # for loops adalah salah satu struktur kontrol yang digunakan untuk melakukan pengulangan pada sebuah urutan data seperti list, tuple, string, atau range. 
#contoh1 list
fruits = ['salak', 'jambu', 'magga','delima']  #membuat list buah-buahan    
for X in fruits:      #melakukan iterasi pada setiap elemen dalam list fruits
    print(X)      #menampilkan setiap elemen dalam list fruits  
    
#contoh2 range
for i in range(5):   #melakukan iterasi dari 0 hingga 4
    print(i)     #menampilkan nilai i pada setiap iterasi yaitu 0,1,2,3,4

#contoh3 string
for char in 'dimas':   #melakukan iterasi pada setiap karakter dalam string
    print(char)     #menampilkan setiap karakter dalam string 'dimas' dalam bentuk vertikal

#contoh4 tuple
colors = ('merah', 'hijau', 'biru')  #membuat tuple warna
for color in colors:   #melakukan iterasi pada setiap elemen dalam tuple colors
    print(color)     #menampilkan setiap elemen dalam tuple colors

'''selain contoh sederhana diatas kita juga bisa memakai else'''

#contoh
for i in range(7):   #melakukan iterasi dari 0 hingga 2
    print(i)
else:
    print('selesai')

'''penjelasan'''
#else pada for loops akan dieksekusi setelah semua iterasi selesai dilakukan. Jadi, setelah loop for selesai menjalankan semua iterasi, blok kode di dalam else akan dijalankan sekali.

'''kita juga bisa menggunakan break pada for loops'''
#contoh
for i in range(10):   #melakukan iterasi dari 0 hingga 9
    if i == 5:     #jika nilai i sama dengan 5
        break     #keluar dari loop
    print(i)     #menampilkan nilai i pada setiap iterasi yaitu 0,1,2,3,4

'''selesai'''
