'''Soal 2 (Range dan Pola Bilangan)
Buat sebuah fungsi bernama bilangan prima(n) yang:
1. Menggunakan range()
2. Mengembalikan list bilangan prima dari 1 sampai n
Kemudian:
1. Panggil fungsi untuk n = 50
2. Tampilkan hasilnya'''
'''jawaban'''

def bilangan_prima(n):
    prima=[]
    for i in range(2,n+1):
        status= True
        for j in range(2,i):
            if i%j == 0:
                status = False
                break
        if status:
            prima.append(i)
    return prima

print(bilangan_prima(50))



