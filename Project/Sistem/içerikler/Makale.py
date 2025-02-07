class makale:
    def __init__(self, yazar,makale_adi, durum, kabul_tarihi, gönderim_tarihi, dil, kelime_sayisi, icerikler=None):
        self.__yazar = yazar
        self.__makale_adi = makale_adi
        self.__durum = durum
        self.__kabul_tarihi = kabul_tarihi
        self.__gönderim_tarihi = gönderim_tarihi
        self.__dil = dil
        self.__kelime_sayisi = kelime_sayisi
        self.__icerikler = icerikler if icerikler else []


    # Getter ve Setter metotları

    def get__yazar(self):
        return self.__yazar
    
    def set__yazar(self, yeni_yazar):
        self.__yazar = yeni_yazar

    def get__makale_adi(self):
        return self.__makale_adi
    
    def set__makale_adi(self, yeni_makale):
        self.__makale_adi = yeni_makale

    def get__durum(self):
        return self.__durum
    
    def set__durum(self, yeni_durum):
        self.__durum = yeni_durum

    def get__kabul_tarihi(self):
        return self.__kabul_tarihi
    
    def set__kabul_tarihi(self, yeni_tarih):
        self.__kabul_tarihi = yeni_tarih

    def get__gönderim_tarihi(self):
        return self.__gönderim_tarihi
    
    def set__gönderim_tarihi(self, yeni_gönderim_tarihi):
        self.__gönderim_tarihi = yeni_gönderim_tarihi

    def get__dil(self):
        return self.__dil
    
    def set__dil(self, yeni_dil):
        self.__dil = yeni_dil

    def get__kelime_sayisi(self):
        return self.__kelime_sayisi
    
    def set__kelime_sayisi(self, yeni_kelime_sayisi):
        self.__kelime_sayisi = yeni_kelime_sayisi

    def get__icerikler(self):
        return self.__icerikler

    def set__icerikler(self, yeni_icerik):
        self.__icerikler = yeni_icerik



    def makale_bilgileri(self):
        """Makale bilgilerini yazdırır."""
        print(f" {self.get_makale_adi()} - {self.get_durum()} - {self.get_kabul_tarihi()} - {self.get_gönderim_tarihi()} - {self.get_dil()} - {self.get_kelime_sayisi()}")
        print("Makale İçerikleri:")
        turler = []
        for icerik in self.get_icerikler():
            if icerik[0] not in turler:
                turler.append(icerik[0])

        for tur in turler:
            print(tur)
            for icerik in self.get_icerikler():
                if icerik[0] == tur:
                    yazarlar = ", ".join(icerik[2])
                    print(f"{icerik[1]} - {yazarlar}")


    def icerik_ekle(self):
        """Kullanıcıdan içerik bilgisi alarak içerikler listesine ekler."""
        tur = input("İçeriğin Türünü Giriniz: ")
        konu = input("İçeriğin Adını Giriniz: ")
        yazarlar = []

        while True:
            yazar = input("Yazar Giriniz: ").strip()
            if yazar:
                yazarlar.append(yazar)
            else:
                print("Yazar adı boş bırakılamaz!")
                continue

            yazarkontrol = input("Başka bir yazar eklemek ister misiniz? (E/H): ").lower()
            if yazarkontrol == "h":
                break

        icerik = [tur, konu, yazarlar]
        self.get_icerikler().append(icerik)
        print("İçerik başarıyla eklendi!")



    def makale_txt_yazdir(self):         
        veri = [self.get_yazar(),self.getmakale_adi(), self.getdurum(),self.getkabul_tarihi(),self.getgönderim_tarihi(), self.getdil(),self.getkelime_sayisi(), self.get_icerikler()]
        with open("makaleler.txt", "a", encoding="utf-8") as dosya:
            dosya.write(f"{veri[0].title()} - {veri[1]} - {veri[2]} - {veri[3]} - {veri[4]} - {veri[5]} - {veri[6]} - {veri[7]}\n")
            print("Kayıt başarılı!")



    def durum_guncelle(self,makale_adi ):
        """
    Kullanıcıdan yeni durum alır ve makaleler.txt dosyasındaki ilgili makalenin durumunu günceller.
    """
        try:
        # Kullanıcıdan yeni durum ve makale adını al
            yeni_durum = input("Makale için yeni durum giriniz (örn. Kabul Edildi, Reddedildi, İnceleme Aşamasında): ").strip()
        # Dosyayı oku ve güncelle
            with open("makaleler.txt", "r", encoding="utf-8") as dosya:
                satirlar = dosya.readlines()

        # Güncellenmiş satırlar için liste
            yeni_satirlar = []
            durum_guncellendi = False

            for satir in satirlar:
                satir_verileri = satir.strip().split(" - ")

            # Makale adı eşleşirse durum güncelle
                if len(satir_verileri) >= 3 and satir_verileri[1].lower() == makale_adi.lower():
                    eski_durum = satir_verileri[2]  # Durum bilgisi, 2. sütunda yer alıyor
                    satir_verileri[2] = yeni_durum  # Yeni durum bilgisiyle değiştir
                    yeni_satirlar.append(" - ".join(satir_verileri) + "\n")
                    durum_guncellendi = True
                    print(f"'{makale_adi}' için durum bilgisi güncellendi: '{eski_durum}' → '{yeni_durum}'")
                else:
                    yeni_satirlar.append(satir)

        # Eğer makale adı bulunamazsa kullanıcıyı bilgilendir
            if not durum_guncellendi:
                print(f"{makale_adi} adlı makale bulunamadı!")

        # Güncellenmiş verileri dosyaya yaz
            with open("makaleler.txt", "w", encoding="utf-8") as dosya:
                dosya.writelines(yeni_satirlar)

        except FileNotFoundError:
            print("makaleler.txt dosyası bulunamadı!")
        except Exception as e:
            print(f"Hata oluştu: {e}")




    def dil_guncelle(self, makale_adi):
        """
    Kullanıcıdan yeni dil alır ve makaleler.txt dosyasındaki ilgili makalenin dil bilgisini günceller.
    """
        try:
        # Kullanıcıdan yeni dil ve makale adını al
            yeni_dil = input("Makale için yeni dil giriniz (örn. Türkçe, İngilizce): ").strip()
        # Dosyayı oku ve güncelle
            with open("makaleler.txt", "r", encoding="utf-8") as dosya:
                satirlar = dosya.readlines()

        # Güncellenmiş satırlar için liste
            yeni_satirlar = []
            dil_guncellendi = False

            for satir in satirlar:
                satir_verileri = satir.strip().split(" - ")

            # Makale adı eşleşirse dil güncelle
                if len(satir_verileri) >= 5 and satir_verileri[1].lower() == makale_adi.lower():
                    eski_dil = satir_verileri[4]  # Dil bilgisi, 4. sütunda yer alıyor
                    satir_verileri[5] = yeni_dil  # Yeni dil bilgisiyle değiştir
                    yeni_satirlar.append(" - ".join(satir_verileri) + "\n")
                    dil_guncellendi = True
                    print(f"'{makale_adi}' için dil bilgisi güncellendi: '{eski_dil}' → '{yeni_dil}'")
                else:
                    yeni_satirlar.append(satir)

        # Eğer makale adı bulunamazsa kullanıcıyı bilgilendir
            if not dil_guncellendi:
                print(f"{makale_adi} adlı makale bulunamadı!")

        # Güncellenmiş verileri dosyaya yaz
            with open("makaleler.txt", "w", encoding="utf-8") as dosya:
                dosya.writelines(yeni_satirlar)

        except FileNotFoundError:
            print("makaleler.txt dosyası bulunamadı!")
        except Exception as e:
            print(f"Hata oluştu: {e}")