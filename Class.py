# ÖDEV 2 , 2. KISIM 

# CLASS ÖRNEĞİ

class hesapIslemleri:
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        print("Hesap İşlemleri başlatıldı...\n")

    def toplama(self):
        print("Toplama işlemi başarıyla yapıldı...\n")
        return self.sayi1 + self.sayi2

    def çıkarma(self):
        print("Çıkarma işlemi başarıyla yapıldı...\n")
        return self.sayi1 - self.sayi2

    def çarpma(self):
        print("Çarpma işlemi başarıyla yapıldı...\n") 
        return self.sayi1 * self.sayi2       

    def bölme(self):
        print("Bölme işlemi başarıyla yapıldı...\n")
        return self.sayi1 / self.sayi2     

    def ikiniciyi_üssüne_al(self):
        print("Üssel işlem başarıyla yapıldı...\n")
        return self.sayi1 ** self.sayi2      

    def birinciyi_üssüne_al(self):
        print("Üssel işlem başarıyla yapıldı...\n")
        return self.sayi2 ** self.sayi1
        

# Sayı1'i Sayı2 nin üssüne yazarak, üslü işlem yaparız.  
hesaplama = hesapIslemleri(4,5)
sonucBul = hesaplama.birinciyi_üssüne_al()
print("Sonuç: "+ str(sonucBul))

# Sayı2'i Sayı1 nin üssüne yazarak, üslü işlem yaparız.  
sonucBul = hesaplama.ikiniciyi_üssüne_al()
print("Sonuç: "+ str(sonucBul))

# Class'ın bu fonksiyonu toplama işlemi yapar.
sonucBul = hesaplama.toplama()
print("Sonuç: "+ str(sonucBul))

# Class'ın bu fonksiyonu çıkarma işlemi yapar.
sonucBul = hesaplama.çıkarma()
print("Sonuç: "+ str(sonucBul))

# Class'ın bu fonksiyonu çarpma işlemi yapar.
sonucBul = hesaplama.çarpma()
print("Sonuç: "+ str(sonucBul))

# Class'ın bu fonksiyonu bölme işlemi yapar.
sonucBul = hesaplama.bölme()
print("Sonuç: "+ str(sonucBul))



# Öğrenci Görüntüleme Class Örneği

class ogrenciListesi:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
               
ogrenci1 = ogrenciListesi(input("İsim: "),input("Soyisim: "))
print(ogrenci1.name,ogrenci1.surname)


# İstatistik Hesaplatma Inheritance İle

import math

class Istatistik(hesapIslemleri):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)

    def ortalamanınKarekoku(self): 
        return math.sqrt((self.sayi1 + self.sayi2)/2)
                  
istatistik = Istatistik(23,11)
sonuc = istatistik.ortalamanınKarekoku()
print(sonuc)