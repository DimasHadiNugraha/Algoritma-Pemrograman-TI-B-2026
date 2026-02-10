'''Soal 5 (Python Module dan Algoritma)
Buat sebuah program Python yang:
1. Menggunakan module math
2. Membuat fungsi jarak(x1, y1, x2, y2) untuk menghitung jarak dua titik pada
bidang Kartesius
3. Menggunakan rumus:
d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

Contoh keluaran:
Jarak = 5.0
'''
import math
def jarak(x1,y1,x2,y2): #membuat fungsi bernama jarak
    return math.sqrt((x2-x1)**2 + (y2-y1)**2) #menghitung dengan mengunakan rumus

print(jarak(1,2,4,6))



        
    
