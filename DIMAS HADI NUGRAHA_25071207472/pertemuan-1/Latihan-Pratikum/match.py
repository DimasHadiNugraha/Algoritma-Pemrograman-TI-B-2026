'''match statement python'''
#jika terlalu banyak kondisi if...elif...else maka bisa menggunakan match statement agar lebih rapi dan mudah dibaca.
#contoh1 match statement
nilai = '70'   #mendefinisikan variabel nilai dengan nilai 'A'
match nilai:   #menggunakan match statement untuk memeriksa nilai
    case 'a':   #jika nilai adalah 'A'
        print('selamat anda mendapat nilai A')   #maka tampilkan pesan mendapat nilai A
    case 'B':   #jika nilai adalah 'B'
        print('selamat anda mendapat nilai B')   #maka tampilkan pesan mendapat nilai B
    case 'C':   #jika nilai adalah 'C'
        print('selamat anda mendapat nilai C')   #maka tampilkan pesan mendapat nilai C
    case _:   #jika tidak ada yang sesuai
        print('maaf nilai anda tidak valid')   #maka tampilkan pesan nilai tidak valid

#catatan:jika ingin blok case gunakan garis bawah (_)

#if statement untuk mengecek kondisi tambahan
#contoh2 match statement dengan if
angka = 15   #mendefinisikan variabel angka dengan nilai 1
match angka:   #menggunakan match statement untuk memeriksa angka
    case x if x < 10:   #jika angka kurang dari 10
        print('angka kurang dari 10')   #maka tampilkan pesan kurang dari 10
    case x if x == 10:   #jika angka sama dengan 10
        print('angka sama dengan 10')   #maka tampilkan pesan sama dengan 10
    case x if x > 10:   #jika angka lebih dari 10
        print('angka lebih dari 10')   #maka tampilkan pesan lebih dari 10