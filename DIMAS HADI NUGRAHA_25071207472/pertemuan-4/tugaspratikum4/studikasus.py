print('=== Program Perhitungan Biaya patungan Bukber===')

try:
    bukber1 = input('berapa orang yang memesan makanan:')
    bukber1 = float(bukber1)

    bukber2 = input('total biaya makanan:')
    bukber2 = float(bukber2)

    jumlah = bukber2 / bukber1
except ValueError:
    print('Masukkan angka yang valid')

except ZeroDivisionError:
    print('tidak ada orang yang memesan')

else:
    print(jumlah)

finally:
    print("terimakasih")
    