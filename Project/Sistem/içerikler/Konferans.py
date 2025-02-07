class konferans:
    def __init__(self,konusmaci, konferans_adi, yer, tarih, saat_bilgisi, katilimcilar, durum, icerikler=None):
        self.__konusmaci = konusmaci
        self.__konferans_adi = konferans_adi
        self.__yer = yer
        self.__tarih = tarih
        self.__saat_bilgisi = saat_bilgisi
        self.__katilimcilar = katilimcilar
        self.__durum = durum
        self.__icerikler = icerikler if icerikler else []


    # Getter ve Setter

    def get__konusmaci(self):
        return self.__konusmaci

    def set__konusmaci(self, yeni_konusmaci):
        self.__konusmaci = yeni_konusmaci

    def get__konferans_adi(self):
        return self.__konferans_adi

    def set__konferans_adi(self, yeni_konferans_adi):
        self.__konferans_adi = yeni_konferans_adi

    def get__yer(self):
        return self.__yer

    def set__yer(self, yeni_yer):
        self.__yer = yeni_yer

    def get__tarih(self):
        return self.__tarih

    def set__tarih(self, yeni_tarih):
        self.__tarih = yeni_tarih

    def get__saat_bilgisi(self):
        return self.__saat_bilgisi

    def set__saat_bilgisi(self, yeni_saat_bilgisi):
        self.__saat_bilgisi = yeni_saat_bilgisi

    def get__katilimcilar(self):
        return self.__katilimcilar

    def set__katilimcilar(self, yeni_katilimcilar):
        self.__katilimcilar = yeni_katilimcilar

    def get__durum(self):
        return self.__durum

    def set__durum(self, yeni_durum):
        self.__durum = yeni_durum

    def get__icerikler(self):
        return self.__icerikler

    def set__icerikler(self, yeni_icerik):
        self.__icerikler = yeni_icerik

  
    def konferans_bilgileri(self):
        """Konferans bilgilerini yazdırır."""
        print(f"{self.get_konferans_adi()} - {self.getyer()} - {self.gettarih()} - {self.getsaat_bilgisi()} - {self.get_durum()}")
        print("Katılımcılar: ", ", ".join(self.get__katilimcilar()))
        print("\nKonferans İçerikleri:")
        turler = []


        for icerik in self.get__icerikler():
            if icerik[0] not in turler:
                turler.append(icerik[0])

        for tur in turler:
            print(tur)
            for icerik in self.get__icerikler():
                if icerik[0] == tur:
                    yapimcilar = ", ".join(icerik[2])
                    print(f"{icerik[1]} - {yapimcilar}")


    def icerik_ekle(self):
        """Konferansa yeni içerik ekler."""
        tur = input("İçeriğin Türünü Giriniz: ")
        konu = input("İçeriğin Konusunu Giriniz: ")
        yapimcilar = []

        while True:
            yapimci = input("Yapımcı Giriniz: ").strip()
            if yapimci:
                yapimcilar.append(yapimci)
            else:
                print("Yapımcı adı boş olamaz!")
                continue

            yapimci_kontrol = input("Başka bir yapımcı eklemek ister misiniz? (E/H): ").lower()
            if yapimci_kontrol == "h":
                break

        icerik = [tur, konu, yapimcilar]
        self.get__icerikler().append(icerik)
        print("Yeni içerik başarıyla eklendi!")


    def konferans_txt_yazdir(self):         
        veri = [self.get_konusmaci(),self.getkonferans_adi(), self.getyer(),self.gettarih(),self.getsaat_bilgisi(), self.getkatilimcilar(),self.getdurum(), self.get_icerikler()]
        with open("konferanslar.txt", "a", encoding="utf-8") as dosya:
            dosya.write(f"{veri[0].title()} - {veri[1]} - {veri[2]} - {veri[3]} - {veri[4]} - {veri[5]} - {veri[6]} - {veri[7]}\n")
            print("Kayıt başarılı!")





    def yer_guncelle(self,konferans_adi):
        """
    Kullanıcıdan yeni yer alır, konferanslar.txt dosyasındaki ilgili kaydın yerini günceller.
    """
        try:
            # Kullanıcıdan yeni yer ve güncellenecek konferans adını al
            yeni_yer = input("Konferans için yeni yeri giriniz: ").strip()

        # Dosyayı oku ve güncelle
            with open("konferanslar.txt", "r", encoding="utf-8") as dosya:
                satirlar = dosya.readlines()

        # Yeni veriler için liste
            yeni_satirlar = []
            yer_guncellendi = False

            for satir in satirlar:
                satir_verileri = satir.strip().split(" - ")

            # Konferans adı eşleşirse yer güncelle
                if len(satir_verileri) >= 3 and satir_verileri[1].lower() == konferans_adi.lower():
                    eski_yer = satir_verileri[2]  # Yer, 2. sütunda yer alıyor
                    satir_verileri[2] = yeni_yer  # Yeri güncelle
                    yeni_satirlar.append(" - ".join(satir_verileri) + "\n")
                    yer_guncellendi = True
                    print(f"'{konferans_adi}' için yer güncellendi: '{eski_yer}' → '{yeni_yer}'")
                else:
                    yeni_satirlar.append(satir)

        # Eğer konferans adı bulunamazsa bilgi ver
            if not yer_guncellendi:
                print(f"{konferans_adi} adlı konferans bulunamadı!")

        # Güncellenmiş verileri dosyaya yaz
            with open("konferanslar.txt", "w", encoding="utf-8") as dosya:
                dosya.writelines(yeni_satirlar)

        except FileNotFoundError:
            print("konferanslar.txt dosyası bulunamadı!")
        except Exception as e:
            print(f"Hata oluştu: {e}")




    def tarih_guncelle(self,konferans_adi):
        """
    Kullanıcıdan yeni tarih bilgisi alır ve konferanslar.txt dosyasındaki ilgili kaydın tarih bilgisini günceller.
    """
        try:
        # Kullanıcıdan yeni tarih ve konferans adı al
            yeni_tarih = input("Konferans için yeni bir tarih giriniz (örn. 2023-12-25): ").strip()
        # Dosyayı oku ve güncelle
            with open("konferanslar.txt", "r", encoding="utf-8") as dosya:
                satirlar = dosya.readlines()

        # Güncellenmiş satırlar için liste
            yeni_satirlar = []
            tarih_guncellendi = False

            for satir in satirlar:
                satir_verileri = satir.strip().split(" - ")

            # Konferans adı eşleşirse tarih güncelle
                if len(satir_verileri) >= 4 and satir_verileri[1].lower() == konferans_adi.lower():
                    eski_tarih = satir_verileri[3]  # Tarih bilgisi, 3. sütunda yer alıyor
                    satir_verileri[3] = yeni_tarih  # Yeni tarih bilgisiyle değiştir
                    yeni_satirlar.append(" - ".join(satir_verileri) + "\n")
                    tarih_guncellendi = True
                    print(f"'{konferans_adi}' için tarih bilgisi güncellendi: '{eski_tarih}' → '{yeni_tarih}'")
                else:
                    yeni_satirlar.append(satir)

        # Eğer konferans adı bulunamazsa kullanıcıyı bilgilendir
            if not tarih_guncellendi:
                print(f"{konferans_adi} adlı konferans bulunamadı!")

        # Güncellenmiş verileri dosyaya yaz
            with open("konferanslar.txt", "w", encoding="utf-8") as dosya:
                dosya.writelines(yeni_satirlar)

        except FileNotFoundError:
            print("konferanslar.txt dosyası bulunamadı!")
        except Exception as e:
            print(f"Hata oluştu: {e}")



    def saat_bilgisi_guncelle(self,konferans_adi):
        """
    Kullanıcıdan yeni saat bilgisi alır ve konferanslar.txt dosyasındaki ilgili kaydın saat bilgisini günceller.
    """
        try:
            # Kullanıcıdan yeni saat ve konferans adı al
            yeni_saat = input("Konferans için yeni bir saat giriniz (örn. 14:00): ").strip()

        # Dosyayı oku ve güncelle
            with open("konferanslar.txt", "r", encoding="utf-8") as dosya:
                satirlar = dosya.readlines()

        # Güncellenmiş satırlar için liste
            yeni_satirlar = []
            saat_guncellendi = False

            for satir in satirlar:
                satir_verileri = satir.strip().split(" - ")

            # Konferans adı eşleşirse saat güncelle
                if len(satir_verileri) >= 5 and satir_verileri[1].lower() == konferans_adi.lower():
                    eski_saat = satir_verileri[4]  # Saat bilgisi, 4. sütunda yer alıyor
                    satir_verileri[4] = yeni_saat  # Yeni saat bilgisiyle değiştir
                    yeni_satirlar.append(" - ".join(satir_verileri) + "\n")
                    saat_guncellendi = True
                    print(f"'{konferans_adi}' için saat bilgisi güncellendi: '{eski_saat}' → '{yeni_saat}'")
                else:
                    yeni_satirlar.append(satir)

        # Eğer konferans adı bulunamazsa kullanıcıyı bilgilendir
            if not saat_guncellendi:
                print(f"{konferans_adi} adlı konferans bulunamadı!")

        # Güncellenmiş verileri dosyaya yaz
            with open("konferanslar.txt", "w", encoding="utf-8") as dosya:
                dosya.writelines(yeni_satirlar)

        except FileNotFoundError:
            print("konferanslar.txt dosyası bulunamadı!")
        except Exception as e:
            print(f"Hata oluştu: {e}")

    def durum_guncelle(self, konferans_adi):
        """
    durum günceller
    """
        try:
            # Kullanıcıdan yeni durum al
            yeni_durum = input("durum gir): ").strip()

        # Dosyayı oku ve güncelle
            with open("konferanslar.txt", "r", encoding="utf-8") as dosya:
                satirlar = dosya.readlines()

        # Güncellenmiş satırlar için liste
            yeni_satirlar = []
            durum_guncellendi = False

            for satir in satirlar:
                satir_verileri = satir.strip().split(" - ")

            # Konferans adı eşleşirse saat güncelle
                if len(satir_verileri) >= 5 and satir_verileri[1].lower() == konferans_adi.lower():
                    eski_durum = satir_verileri[6]  # Saat bilgisi, 4. sütunda yer alıyor
                    satir_verileri[6] = yeni_durum  # Yeni saat bilgisiyle değiştir
                    yeni_satirlar.append(" - ".join(satir_verileri) + "\n")
                    durum_guncellendi = True
                    print(f"'{konferans_adi}' için durum bilgisi güncellendi: '{eski_durum}' → '{yeni_durum}'")
                else:
                    yeni_satirlar.append(satir)

        # Eğer konferans adı bulunamazsa kullanıcıyı bilgilendir
            if not durum_guncellendi:
                print(f"{konferans_adi} adlı konferans bulunamadı!")

        # Güncellenmiş verileri dosyaya yaz
            with open("konferanslar.txt", "w", encoding="utf-8") as dosya:
                dosya.writelines(yeni_satirlar)

        except FileNotFoundError:
            print("konferanslar.txt dosyası bulunamadı!")
        except Exception as e:
            print(f"Hata oluştu: {e}")  