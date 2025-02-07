from abc import ABC, abstractmethod
class kisi:
    def __init__(self,isim,soyisim,kullanici_adi,sifre,yetki):
        self.__isim = isim
        self.__soyisim = soyisim
        self.__kullanici_adi = kullanici_adi
        self.__sifre = sifre
        self.__yetki = yetki

    def isim_goster(self):
        return self.__isim
    def soyisim_goster(self):
        return self.__soyisim
    def kullanici_adi_goster(self):
        return self.__kullanici_adi
    def sifre_goster(self):
        return self.__sifre
    def yetki_goster(self):
        return self.__yetki
   
    def isim_degistir(self,yeni):
        self.__isim = yeni
    def soyisim_degistir(self,yeni):
        self.__soyisim = yeni
    def kullanici_adi_degistir(self,yeni):
        self.__kullanici_adi = yeni
    def sifre_degistir(self,yeni):
        self.__sifre = yeni
    def yetki_degistir(self,yeni):
        self.__yetki = yeni

    @abstractmethod
    def makaleleri_goruntule(self):
        pass
    
    @abstractmethod
    def konferanslari_goruntule(self):
        pass
    @abstractmethod
    def dergileri_goruntule(self):
        pass



 
    
