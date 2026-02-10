''' function dipython dengan argumen'''
    #fungsi dengan argumen adalah fungsi yang menerima inputan nilai saat fungsi tersebut dipanggil. Argumen ini dapat digunakan di dalam fungsi untuk melakukan operasi atau perhitungan berdasarkan nilai yang diberikan.
#contoh1 fungsi dengan argumen
def nama_mahasiswa(name):   #mendefinisikan fungsi dengan argumen name
    print(name +"mahasiswa ti b")   #menggunakan argumen name di
nama_mahasiswa('dimas')   #memanggil fungsi dengan memberikan argumen 'dimas'
nama_mahasiswa('eng')   #memanggil fungsi dengan memberikan argumen 'eng'
nama_mahasiswa('fatih') #memanggil fungsi dengan memnerikan argumen 'fatih'

'''fungi dengan lebih dari satu argumen'''
#jika  ingin fungsi kita ingin 2 argumen kita juga harus memanggilnya dengan 2 argumen
#contoh2 fungsi dengan 2 argumen
def nama_lengkap(dimas,nugraha):   #mendefinisikan fungsi dengan 2 argumen dimas dan nugraha
    print(dimas + ' ' + nugraha)   #menggunakan kedua argumen di dalam fungsi
nama_lengkap('dimas','nugraha')    #memanggil fungsi dengan memberikan 2 argumen

'''defaul parameter value'''
    #kita juga bisa memberikan nilai default pada argumen fungsi. Jika argumen tersebut tidak diberikan saat pemanggilan fungsi, maka nilai default akan digunakan.
#contoh3 fungsi dengan default parameter value
def perkenalan(nama, umur=20):   #mendefinisikan fungsi dengan argumen nama dan umur dengan nilai default 20
    print('nama saya ' + nama + ', umur saya ' + str(umur) + ' tahun')   #menggunakan kedua argumen di dalam fungsi         
perkenalan('dimas')   #memanggil fungsi hanya dengan memberikan argumen nama
perkenalan('eng', 22)   #memanggil fungsi dengan memberikan kedua argumen  

'''retrun value '''
    #fungsi juga bisa mengembalikan nilai menggunakan perintah return. Nilai yang dikembalikan dapat digunakan di luar fungsi.
#contoh4 fungsi dengan return value
def tambah(a, b):   #mendefinisikan fungsi dengan 2 argumen a dan b
    return a + b   #mengembalikan hasil penjumlahan a dan b     

hasil = tambah(5, 10)   #memanggil fungsi dan menyimpan hasilnya dalam variabel hasil
print(hasil)

'''selesai'''