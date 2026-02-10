'''1.3 Soal 3 (Rekursi - Penjumlahan Digit)
Buat sebuah fungsi rekursif bernama jumlah digit(n) yang:
1. Menghitung jumlah seluruh digit dari sebuah bilangan
2. Menggunakan konsep rekursi
Contoh:
Input: 1234
Output: 10
'''
'''jawaban'''

def jumlah_digit(n):
    if n == 0:
        return 0
    else:
        return (n % 10)+jumlah_digit(n//10)
    
angka = int(input("masukan sebuah angka:"))
print('jumlah:',jumlah_digit(angka)) 

    