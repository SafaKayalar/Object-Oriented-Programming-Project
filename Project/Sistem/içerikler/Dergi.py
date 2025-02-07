class dergi:
    def __init__(self, dergi_adi, yayin_yili, cilt, tur ,dil, editor,yayinci, icerikler=None):
        self.__dergi_adi = dergi_adi
        self.__yayin_yili = yayin_yili
        self.__cilt = cilt
        self.__tur = tur
        self.__dil = dil
        self.__editor = editor
        self.__yayinci = yayinci
        self.__icerikler = icerikler if icerikler else []

    # Getter ve Setter metotları
    def get__dergi_adi(self):
        return self.__dergi_adi

    def set__dergi_adi(self, yeni_dergi_adi):
        self.__dergi_adi = yeni_dergi_adi

    def get__yayin_yili(self):
        return self.__yayin_yili

    def set__yayin_yili(self, yeni_yayin_yili):
        self.__yayin_yili = yeni_yayin_yili

    def get__cilt(self):
        return self.__cilt

    def set__cilt(self, yeni_cilt):
        self.__cilt = yeni_cilt

    def get__tur(self):
        return self.__tur

    def set__tur(self, yeni_tur):
        self.__tur = yeni_tur

    def get__dil(self):
        return self.__dil

    def set__dil(self, yeni_dil):
        self.__dil = yeni_dil

    def get__editor(self):
        return self.__editor

    def set__editor(self, yeni_editor):
        self.__editor = yeni_editor

    def get__yayinci(self):
        return self.__yayinci

    def set__yayinci(self, yeni_yayinci):
        self.__yayinci = yeni_yayinci

    def get__icerikler(self):
        return self.__icerikler

    def set__icerikler(self, yeni_icerikler):
        if not isinstance(yeni_icerikler, list):
            raise ValueError("İçerikler bir liste olmalıdır!")
        self.__icerikler = yeni_icerikler



    def dergi_bilgileri(self):
        """Dergi bilgilerini ve içerikleri yazdırır."""
        print(f"{self.get_dergi_adi()} - {self.getyayin_yili()} - Cilt: {self.getcilt()} - Sayı: {self.get_tur()}")
        print("\nİçerikler:")
        turler = []
        for icerik in self.get__icerikler():
            if icerik[0] not in turler:
                turler.append(icerik[0])

        for tur in turler:
            print(tur)
            for icerik in self.get__icerikler():
                if icerik[0] == tur:
                    yazarlar = ", ".join(icerik[2])
                    print(f"{icerik[1]} - {yazarlar}")

    def icerik_ekle(self):
        """Kullanıcıdan içerik bilgisi alarak içerikler listesine ekler."""
        tur = input("İçeriğin Türünü Giriniz: ")
        baslik = input("İçeriğin Adını Giriniz: ")
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

        icerik = [tur, baslik, yazarlar]
        self.get__icerikler().append(icerik)
        print("İçerik başarıyla eklendi!")



    def dergi_txt_yazdir(self):         
        veri = [self.get_dergi_adi(), self.getyayin_yili(),self.getcilt(),self.gettur(), self.getdil (),self.geteditor(), self.getyayinci(),self.get_icerikler()]
        with open("dergiler.txt", "a", encoding="utf-8") as dosya:
            dosya.write(f"{veri[0].title()} - {veri[1]} - {veri[2]} - {veri[3]} - {veri[4]} - {veri[5]} - {veri[6]} - {veri[7]}\n")
            print("Kayıt başarılı!")



    def tur_guncelle(self,dergi_adi):
        """
    Kullanıcıdan yeni tür alır ve dergiler.txt dosyasındaki ilgili derginin tür bilgisini günceller.
    """
        try:
        # Kullanıcıdan yeni tür ve dergi adını al
            yeni_tur = input("Dergi için yeni tür giriniz (örn. Bilim, Sanat, Teknoloji): ").strip()

        # Dosyayı oku ve güncelle
            with open("dergiler.txt", "r", encoding="utf-8") as dosya:
                satirlar = dosya.readlines()

        # Güncellenmiş satırlar için liste
            yeni_satirlar = []
            tur_guncellendi = False

            for satir in satirlar:
                satir_verileri = satir.strip().split(" - ")

            # Dergi adı eşleşirse tür güncelle
                if len(satir_verileri) >= 4 and satir_verileri[0].lower() == dergi_adi.lower():
                    eski_tur = satir_verileri[3]  # Tür bilgisi, 3. sütunda yer alıyor
                    satir_verileri[3] = yeni_tur  # Yeni tür bilgisiyle değiştir
                    yeni_satirlar.append(" - ".join(satir_verileri) + "\n")
                    tur_guncellendi = True
                    print(f"'{dergi_adi}' için tür bilgisi güncellendi: '{eski_tur}' → '{yeni_tur}'")
                else:
                    yeni_satirlar.append(satir)

        # Eğer dergi adı bulunamazsa kullanıcıyı bilgilendir
            if not tur_guncellendi:
                print(f"{dergi_adi} adlı dergi bulunamadı!")

        # Güncellenmiş verileri dosyaya yaz
            with open("dergiler.txt", "w", encoding="utf-8") as dosya:
                dosya.writelines(yeni_satirlar)

        except FileNotFoundError:
            print("dergiler.txt dosyası bulunamadı!")
        except Exception as e:
            print(f"Hata oluştu: {e}")






    def dil_guncelle(self,dergi_adi):
        """
    Kullanıcıdan yeni dil alır ve dergiler.txt dosyasındaki ilgili derginin dil bilgisini günceller.
    """
        try:
        # Kullanıcıdan yeni dil ve dergi adını al
            yeni_dil = input("Dergi için yeni dil giriniz (örn. Türkçe, İngilizce): ").strip()
        # Dosyayı oku ve güncelle
            with open("dergiler.txt", "r", encoding="utf-8") as dosya:
                satirlar = dosya.readlines()

        # Güncellenmiş satırlar için liste
            yeni_satirlar = []
            dil_guncellendi = False

            for satir in satirlar:
                satir_verileri = satir.strip().split(" - ")

            # Dergi adı eşleşirse dil güncelle
                if len(satir_verileri) >= 5 and satir_verileri[0].lower() == dergi_adi.lower():
                    eski_dil = satir_verileri[4]  # Dil bilgisi, 4. sütunda yer alıyor
                    satir_verileri[4] = yeni_dil  # Yeni dil bilgisiyle değiştir
                    yeni_satirlar.append(" - ".join(satir_verileri) + "\n")
                    dil_guncellendi = True
                    print(f"'{dergi_adi}' için dil bilgisi güncellendi: '{eski_dil}' → '{yeni_dil}'")
                else:
                    yeni_satirlar.append(satir)

        # Eğer dergi adı bulunamazsa kullanıcıyı bilgilendir
            if not dil_guncellendi:
                print(f"{dergi_adi} adlı dergi bulunamadı!")

        # Güncellenmiş verileri dosyaya yaz
            with open("dergiler.txt", "w", encoding="utf-8") as dosya:
                dosya.writelines(yeni_satirlar)

        except FileNotFoundError:
            print("dergiler.txt dosyası bulunamadı!")
        except Exception as e:
            print(f"Hata oluştu: {e}")




    def yayinci_guncelle(self):
        """
    Kullanıcıdan yeni yayıncı alır ve dergiler.txt dosyasındaki ilgili derginin yayıncı bilgisini günceller.
    """
        try:
        # Kullanıcıdan yeni yayıncı ve dergi adını al
            yeni_yayinci = input("Dergi için yeni yayıncı giriniz: ").strip()
            dergi_adi = input("Yayıncı bilgisi güncellenecek derginin adını giriniz: ").strip()

        # Dosyayı oku ve güncelle
            with open("dergiler.txt", "r", encoding="utf-8") as dosya:
                satirlar = dosya.readlines()

        # Güncellenmiş satırlar için liste
            yeni_satirlar = []
            yayinci_guncellendi = False

            for satir in satirlar:
                satir_verileri = satir.strip().split(" - ")

            # Dergi adı eşleşirse yayıncı bilgisi güncelle
                if len(satir_verileri) >= 7 and satir_verileri[0].lower() == dergi_adi.lower():
                    eski_yayinci = satir_verileri[6]  # Yayıncı bilgisi, 6. sütunda yer alıyor
                    satir_verileri[6] = yeni_yayinci  # Yeni yayıncı bilgisiyle değiştir
                    yeni_satirlar.append(" - ".join(satir_verileri) + "\n")
                    yayinci_guncellendi = True
                    print(f"'{dergi_adi}' için yayıncı bilgisi güncellendi: '{eski_yayinci}' → '{yeni_yayinci}'")
                else:
                    yeni_satirlar.append(satir)

        # Eğer dergi adı bulunamazsa kullanıcıyı bilgilendir
            if not yayinci_guncellendi:
                print(f"{dergi_adi} adlı dergi bulunamadı!")

        # Güncellenmiş verileri dosyaya yaz
            with open("dergiler.txt", "w", encoding="utf-8") as dosya:
                dosya.writelines(yeni_satirlar)

        except FileNotFoundError:
            print("dergiler.txt dosyası bulunamadı!")
        except Exception as e:
            print(f"Hata oluştu: {e}")