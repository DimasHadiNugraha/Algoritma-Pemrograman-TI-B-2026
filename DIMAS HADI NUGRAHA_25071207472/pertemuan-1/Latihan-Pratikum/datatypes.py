'''datatypes pada python adalah tipe data yang
digunakan untuk menyimpan berbagai jenis data'''

#untuk mengakses tipe data pada python bisa menggunakan fungsi type()

#contoh1 
tipe1 = '1'
tipe2 = 1
tipe3 = 1,4
tipe4 = True
tipe5 = [1,2,3,4,5]
tipe6 = ['dimas',2,3]
tipe7 = (1,2,3,4,5)
tipe8 = {
       'nama': 'dimas',
       'kelas':'TI B',
       'nim' : 25071207472,
       'mahasiswa aktif': True
}
#menampilkan tipe data dari variabel secara langsung
print(type(tipe1))
print(type(tipe2))
print(type(tipe3))
print(type(tipe4))
print(type(tipe5))
print(type(tipe6))
print(type(tipe7))
print(type(tipe8))


#selain menampilkan tipe data kita juga bisa menampilkan nilai dari variabel tersebut
print(tipe6[0])
print(tipe7[2])
print(tipe8['kelas'])
print(tipe8['nim'])

'''selesai'''