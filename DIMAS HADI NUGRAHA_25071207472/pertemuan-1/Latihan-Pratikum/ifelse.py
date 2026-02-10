'''if...else statement pada python'''     
    #if statment mengunakan logika matematika seperti lebih dari (>), kurang dari (<), sama dengan (==), lebih dari sama dengan (>=), kurang dari sama dengan (<=), tidak sama dengan (!=) untuk membandingkan nilai.
#contoh1
nilai = 75   #mendefinisikan variabel nilai dengan nilai 75
if nilai >= 60:   #jika nilai lebih dari atau sama dengan 60
    print('selamat anda lulus')   #maka tampilkan pesan lulus   
else:   #jika tidak
    print('maaf anda tidak lulus')   #maka tampilkan pesan tidak lulus

#contoh2 if statment
nilai = 85   #mendefinisikan variabel nilai dengan nilai 85
if nilai >= 80:   #jika nilai lebih dari atau sama dengan 80
    print('selamat anda mendapat nilai A')   #maka tampilkan pesan mendapat nilai A

#contoh3 multiple statment if
umur = 20   #mendefinisikan variabel umur dengan nilai 20
if umur < 17:   #jika umur kurang dari 17
    print('anda masih dibawah umur')   #maka tampilkan pesan dibawah umur 

 #elif statment
#elif digunakan jika pernyataan if sebelumnya tidak terpenuhi dan ingin memeriksa kondisi lain.
#contoh4 elif statment

x = 10   #mendefinisikan variabel x dengan nilai 10
z = 5    #mendefinisikan variabel z dengan nilai 5
if x > z:   #jika x lebih dari z
    print('x lebih besar dari z')   #maka tampilkan pesan x lebih besar dari z
elif x == z:   #jika x sama dengan z
    print('x sama dengan z')   #maka tampilkan pesan x sama dengan z


 #else statment
#digunakan jika semua pernyataan if dan elif sebelumnya tidak terpenuhi
#contoh5 else statment
x = 7   #mendefinisikan variabel angka dengan nilai 7
y = 10   #mendefinisikan variabel y dengan nilai 10
if x > y:   #jika x lebih dari y
    print('x lebih besar dari y')   #maka tampilkan pesan x lebih besar dari y
elif x == y:   #jika x sama dengan y
    print('x sama dengan y')   #maka tampilkan pesan x sama dengan y
else:   #jika tidak
    print('x kurang dari y')   #maka tampilkan pesan x kurang dari y

'''selesai'''
