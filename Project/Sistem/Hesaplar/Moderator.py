from .Kisi import kisi
class moderator(kisi):
    def __init__(self, isim, soyisim, kullanici_adi, sifre, yetki = "moderator"):
        super().__init__(isim, soyisim, kullanici_adi, sifre, yetki)

    def hesabimi_sil(self):
        silinecek_kullanici_adi = self.kullanici_adi_goster()
        with open("hesaplar.txt", "r", encoding="utf-8") as dosya:
            satirlar = dosya.readlines()
        yeni_satirlar = []
        for satir in satirlar:
            parcalar = [parca.strip() for parca in satir.split("-")]
            if silinecek_kullanici_adi not in parcalar:
                yeni_satirlar.append(satir)

        with open("hesaplar.txt", "w", encoding="utf-8") as dosya:
            dosya.writelines(yeni_satirlar)
        print("Hesabınız başarıyla silindi.")
   
    @staticmethod
    def yazarlari_goruntule():
        with open("hesaplar.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya:
                parcalar = [parca.strip() for parca in satir.split("-")]
                if len(parcalar) >= 5:
                    if parcalar[4] == "yazar":
                        print(f"{parcalar[0]} {parcalar[1]}")  

    @staticmethod
    def uyeleri_goruntule():
        with open("hesaplar.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya:
                # Satırı '-' işaretine göre parçala
                parcalar = [parca.strip() for parca in satir.split("-")]
                if len(parcalar) >= 5:
                    if parcalar[4] == "uye":
                        print(f"{parcalar[0]} {parcalar[1]}")
    @staticmethod
    def terfi_ettir():
        with open("basvurular.txt", "r", encoding="utf-8") as dosya:
            basvurular = dosya.readlines()
        print("Başvurular:")
        for index, satir in enumerate(basvurular, start=1):
            parçalar = satir.split(" - ")
            if len(parçalar) >= 2:
                print(f"{index} - {parçalar[0].strip()} - {parçalar[1].strip()}")
        try:
            indis = int(input("Terfi ettireceğiniz başvuruyu seçiniz (İndeks numarası): ")) - 1  
            if indis < 0 or indis >= len(basvurular):
                print("Geçersiz indeks.")
                return
            basvuru = basvurular[indis]
            parçalar = basvuru.split(" - ")
            isim_soyisim = parçalar[0].strip()
            with open("hesaplar.txt", "r", encoding="utf-8") as dosya:
                satirlar = dosya.readlines()
            for index, satir in enumerate(satirlar):
                parçalar_hesap = satir.split(" - ")
                if len(parçalar_hesap) > 4:
                    isim_soyisim_hesap = f"{parçalar_hesap[0].strip()} {parçalar_hesap[1].strip()}"
                    if isim_soyisim == isim_soyisim_hesap and "uye" in parçalar_hesap[-1].strip():
                        parçalar_hesap[-1] = "yazar\n"
                        satirlar[index] = " - ".join(parçalar_hesap)
            with open("hesaplar.txt", "w", encoding="utf-8") as dosya:
                dosya.writelines(satirlar)
            basvurular.pop(indis)
            with open("basvurular.txt", "w", encoding="utf-8") as dosya:
                dosya.writelines(basvurular)
            print(f"{isim_soyisim} başarıyla 'yazar' olarak terfi ettirildi ve başvuru silindi.")
        except ValueError:
            print("Geçersiz giriş. Lütfen geçerli bir indeks numarası girin.")
        except IndexError:
            print("Geçersiz indeks. Lütfen doğru bir sayı girin.")

    def makaleleri_goruntule(self):
            try:
                with open("makaleler.txt", "r", encoding="utf-8 \n" ) as dosya:
                    print("=== Makaleler ===")
                    for satir in dosya:
                        satir_verileri = satir.strip().split(" - ")
                        if len(satir_verileri) >= 3:  # En az 3 sütun bekleniyor
                            print(f"Yazar: {satir_verileri[0]}")
                            print(f"Makale Başlığı: {satir_verileri[1]}")
                            print(f"Özet: {satir_verileri[2]}")
                            print("-" * 30)
                        else:
                            print(f"Hatalı veri formatı: {satir}")
            except FileNotFoundError:
                print("makaleler.txt dosyası bulunamadı!")
            except Exception as e:
                print(f"Hata oluştu: {e}")

    def konferanslari_goruntule(self):
        try:
            with open("konferanslar.txt", "r", encoding="utf-8") as dosya:
                print("=== Konferanslar ===")
                for satir in dosya:
                    satir_verileri = satir.strip().split(" - ")
                    if len(satir_verileri) >= 4:  # En az 4 sütun bekleniyor
                        print(f"Konferans Adı: {satir_verileri[1]}")
                        print(f"Yer: {satir_verileri[2]}")
                        print(f"Tarih: {satir_verileri[3]}")
                        print(f"Katılımcılar: {satir_verileri[5]}")
                        print("-" * 30)
                    else:
                        print(f"Hatalı veri formatı: {satir}")
        except FileNotFoundError:
            print("konferanslar.txt dosyası bulunamadı!")
        except Exception as e:
            print(f"Hata oluştu: {e}")

    def dergileri_goruntule(self):
        try:
            with open("dergiler.txt", "r", encoding="utf-8") as dosya:
                print("=== Dergiler ===")
                for satir in dosya:
                    satir_verileri = satir.strip().split(" - ")
                    if len(satir_verileri) >= 6:  # En az 6 sütun bekleniyor
                        print(f"Dergi Adı: {satir_verileri[0]}")
                        print(f"Yayın Yılı: {satir_verileri[1]}")
                        print(f"Cilt: {satir_verileri[2]}")
                        print(f"Dil: {satir_verileri[4]}")
                        print(f"Editör: {satir_verileri[5]}")
                        print(f"İçerik: {satir_verileri[6]}")
                        print("-" * 30)
                    else:
                        print(f"Hatalı veri formatı: {satir}")
        except FileNotFoundError:
            print("dergiler.txt dosyası bulunamadı!")
        except Exception as e:
            print(f"Hata oluştu: {e}")

    def kullanici_adimi_degistir(self, yeni): 
        yeni_ad = yeni
        print(f"Yeni kullanıcı adı: {yeni_ad}")
        with open("hesaplar.txt", "r", encoding="utf-8") as dosya:
            mevcut_veriler = dosya.readlines()
        for satir in mevcut_veriler:
            veriler = satir.strip().split(" - ") 
            if len(veriler) >= 3 and veriler[2] == yeni_ad:  
                print("Bu kullanıcı adı zaten var!")
                return
        for i, satir in enumerate(mevcut_veriler):
            veriler = satir.strip().split(" - ")  
            if len(veriler) >= 3:  
                eski_kullanici_adi = veriler[2]  
                if eski_kullanici_adi == self.kullanici_adi_goster():
                    print(f"Eski kullanıcı adı: {eski_kullanici_adi} -> Yeni kullanıcı adı: {yeni_ad}")
                    veriler[2] = yeni_ad  
                    mevcut_veriler[i] = " - ".join(veriler) + "\n"  
        with open("hesaplar.txt", "w", encoding="utf-8") as dosya:
            dosya.writelines(mevcut_veriler)
        print(f"Kullanıcı adı başarıyla '{yeni_ad}' olarak değiştirildi.")
        self.kullanici_adi_degistir(yeni)

    def sifremi_degistir(self, yeni_sifre):
        print(f"Yeni şifre: {yeni_sifre}")
        with open("hesaplar.txt", "r", encoding="utf-8") as dosya:
            mevcut_veriler = dosya.readlines()
        kullanici_bulundu = False
        for i, satir in enumerate(mevcut_veriler):
            veriler = satir.split(" - ")
            eski_kullanici_adi = veriler[2]
            if eski_kullanici_adi == self.kullanici_adi_goster():
                veriler[3] = yeni_sifre  # Şifreyi 3. indisteki değeri güncelle
                mevcut_veriler[i] = " - ".join(veriler)
                kullanici_bulundu = True
                break
        if not kullanici_bulundu:
            print("Kullanıcı adı bulunamadı!")
            return
        with open("hesaplar.txt", "w", encoding="utf-8") as dosya:
            dosya.writelines(mevcut_veriler)
        print("Şifre başarıyla güncellendi.")  

           

