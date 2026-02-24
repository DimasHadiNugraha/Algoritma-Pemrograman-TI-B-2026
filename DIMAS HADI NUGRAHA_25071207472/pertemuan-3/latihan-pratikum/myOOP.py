'''A.INHERITANCE(PERWARISAN)'''
class produk():
    def __init__(self,nama_pruduk,harga):
        self.nama_produk = nama_pruduk
        self.harga = harga
    def info_produk(self):
        print(self.nama_produk,self.harga)

class produkElektronik(produk):
    def __init__(self,nama_pruduk, harga,garansi):
        super().__init__(nama_pruduk,harga)
        self.tahun = garansi
    def info_produk(self):
        print(self.nama_produk,"seharga",self.harga,"dengan garansi",self.tahun,"tahun")


class produkmakanan(produk):
    def __init__(self,nama_pruduk, harga,tanggal_kadaluarsa):
        super().__init__(nama_pruduk,harga)
        self.tahun = tanggal_kadaluarsa
    def info_produk(self):
        print(self.nama_produk,"seharga",self.harga,"kadaluarsa",self.tahun)

print('----soal A----')
produk1 = produkElektronik("tv", "3.000.000", 2)
produk1.info_produk()
produk2= produkmakanan("roti","15.000","12-12-2025")
produk2.info_produk()


'''B.POLYMORPHISM'''

class notifikasi:    
    def kirim(self):
        return("megirim notifikasi umum")

class email(notifikasi):
    def kirim(self):
        return("mengirim notifikasi lewat email")
    
class sms(notifikasi):
    def kirim(self):
        return("mengirim notifikasi memlakui sms")
        
notif1 = email()
notif2 = sms()

print('----soal B----')
print(notif1.kirim())
print(notif2.kirim())

'''C.ENCAPSULATION'''

class Mahasiswa:
    def __init__(self):
        self.__nilai = 0

    def set_nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai = nilai
            return "Nilai berhasil disimpan"
        else:
            return "Nilai tidak valid"

    def get_nilai(self):
        return self.__nilai