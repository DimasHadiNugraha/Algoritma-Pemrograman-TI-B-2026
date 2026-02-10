'''numbers pada python'''
    #tipe data numbers pada python adalah tipe data yang digunakan untuk menyimpan nilai numerik seperti bilangan bulat (integer), bilangan desimal (float), dan bilangan kompleks (complex).
#contoh1 tipe data integer
'''integer adalah tipe data bilangan bulat mau positif atau negatif dan tak terhingga'''
a = 1
b = -5
c = 12345678
print(type(a))  #hasilnya adalah <class 'int'>
print(type(b))  #hasilnya adalah <class 'int'> 
print(type(c))  #hasilnya adalah <class 'int'>

#contoh2 tipe data float
'''float adalah tipe data bilangan desimal atau bilangan pecahan'''
x = 5.7
y = -3.14
z = 0.0
print(type(x))  #hasilnya adalah <class 'float'>
print(type(y))  #hasilnya adalah <class 'float'>
print(type(z))  #hasilnya adalah <class 'float'>

#contoh3 tipe data complex
'''complex adalah tipe data bilangan kompleks yang terdiri dari bagian real dan bagian imajiner'''
p = 2 + 3j
q = -1 - 4j
r = 0 + 0j
print(type(p))  #hasilnya adalah <class 'complex'>
print(type(q))  #hasilnya adalah <class 'complex'>
print(type(r))  #hasilnya adalah <class 'complex'>

#contoh4 type conversion
'''type conversion adalah mengubah dari satu tipe data numbers ke tipe data numbers lainnya'''
no_int = 10 #variabel dengan tipe data integer
no_float = float(no_int)  #mengubah integer ke float
print(no_float)  #hasilnya adalah 10.0

'''selesai'''  