import sys

class menu:
    def __init__(self, hesaplar, icerikler):
        self.hesaplar = hesaplar
        self.icerikler = icerikler
        self.nesne = None
        self.eser = None

    def icerik(self, hesaplar, icerikler):
        while True:    
            print("")
            print("")
            print("")
            print("")
            print("Yapmak istediğiniz işlemi seçiniz: ")
            print(f"1- Kullanıcı adı değiştir: ")
            print(f"2- Şifre değiştir: ")
            print(f"3- Hesabımı sil: ")
            print(f"4- Dergileri gör: ")
            print(f"5- Makaleleri gör: ")
            print(f"6- Konferansları gör: ")
            if type(self.nesne).__name__ == "uye":
                print("7- Yazarları görüntüle")
                print("8- Moderatörleri görüntüle: ")
                print("9- Yazarlık Başvurusu yap: ")
            elif type(self.nesne).__name__ == "icerik_ureticisi":
                print("7- Moderatörleri görüntüle")
                print("8- Eserlerimi Görüntüle: ")
                print("9- İçeriklerimde güncelleme yap")

            elif type(self.nesne).__name__ == "moderator":
                print("7- Yazarları görüntüle: ")
                print("8- Üyeleri görüntüle: ")
                print("9- Terfi ettir: ")
            print(f"10- Çıkış yap: ")     
            seciminiz = input("Yapmak istediğiniz işlemi seçiniz: ")
            if seciminiz == "1":
                kull_adi = input("Yeni kullanıcı adınızı giriniz: ")
                with open("hesaplar.txt", "r", encoding="utf-8") as dosya:
                    mevcut_veriler = dosya.readlines()
                for satir in mevcut_veriler:
                    if kull_adi in satir.split():
                        print("Bu kullanıcı adı zaten var!")
                else:            
                    self.nesne.kullanici_adimi_degistir(kull_adi)   
            elif seciminiz == "2":
                yeni_sifre = input("Yeni şifrenizi giriniz: ")
                self.nesne.sifremi_degistir(yeni_sifre)   
            elif seciminiz == "3":
                self.nesne.hesabimi_sil()
                self.giris_ekrani()
            elif seciminiz == "4":
                self.nesne.dergileri_goruntule()
            elif seciminiz == "5":
                self.nesne.makaleleri_goruntule()
            elif seciminiz == "6":
                self.nesne.konferanslari_goruntule()
            elif seciminiz == "7":
                if type(self.nesne).__name__ == "uye":
                    self.nesne.yazarlari_goruntule()
                elif type(self.nesne).__name__ == "icerik_ureticisi":   
                    self.nesne.moderatorleri_goruntule()
                elif type(self.nesne).__name__ == "moderator":
                    self.nesne.yazarlari_goruntule()
            elif seciminiz == "8":
                if type(self.nesne).__name__ == "uye":
                    self.nesne.moderatorleri_goruntule()
                elif type(self.nesne).__name__ == "icerik_ureticisi":   
                    self.nesne.iceriklerimi_goruntule() 
                elif type(self.nesne).__name__ == "moderator":
                    self.nesne.uyeleri_goruntule()
            elif seciminiz == "9":
                if type(self.nesne).__name__ == "uye":
                    self.nesne.yazarlik_basvurusu_yap()
                elif type(self.nesne).__name__ == "moderator":
                    self.nesne.terfi_ettir()         
                elif type(self.nesne).__name__ == "icerik_ureticisi":   
                    eserlerim = self.nesne.icerik_islemleri() 
                    for index,eser in enumerate(eserlerim,start=1):
                        print(f"{index} - {eser[1]}")
                    guncellenecek = int(input("Hangi Eserinizi Güncellemek İstiyorsunuz? ")) - 1
                    secilen_eser = eserlerim[guncellenecek]       
                    isim = secilen_eser[1].split(" - ")[0] 
                    print(isim)
                    if secilen_eser[0] == "Dergi":
                        self.eser = icerikler[0](secilen_eser[1].split(" - ")[0] ,secilen_eser[1].split(" - ")[1] ,secilen_eser[1].split(" - ")[2] ,secilen_eser[1].split(" - ")[3] ,secilen_eser[1].split(" - ")[4] ,secilen_eser[1].split(" - ")[5] ,secilen_eser[1].split(" - ")[6] ,secilen_eser[1].split(" - ")[7])  
                        print("Eserde güncellemek istediğiniz şeyi giriniz: ")
                        print("1- Dil güncelle: ")
                        print("2- Tür güncelle: ")
                        guncellenecek_indis = input("Seçiminiz: ")
                        if guncellenecek_indis == "1":
                            self.eser.dil_guncelle(secilen_eser[1].split(" - ")[0])
                        elif guncellenecek_indis == "2":
                            self.eser.tur_guncelle(secilen_eser[1].split(" - ")[0])                           
                    elif secilen_eser[0] == "Konferans":
                        self.eser = icerikler[1](secilen_eser[1].split(" - ")[0] ,secilen_eser[1].split(" - ")[1] ,secilen_eser[1].split(" - ")[2] ,secilen_eser[1].split(" - ")[3] ,secilen_eser[1].split(" - ")[4] ,secilen_eser[1].split(" - ")[5] ,secilen_eser[1].split(" - ")[6] ,secilen_eser[1].split(" - ")[7])     
                        print("Eserde güncellemek istediğiniz şeyi giriniz: ")
                        print("1- Durum güncelle: ")
                        print("2- Saat güncelle: ")
                        print("3- Tarih güncelle: ")
                        print("4- Yer güncelle: ")
                        guncellenecek_indis = input("Seçiminiz: ")
                        if guncellenecek_indis == "1":
                            self.eser.durum_guncelle(secilen_eser[1].split(" - ")[1])
                        elif guncellenecek_indis == "2":
                            self.eser.saat_bilgisi_guncelle(secilen_eser[1].split(" - ")[1])  
                        elif guncellenecek_indis == "3":
                            self.eser.tarih_guncelle(secilen_eser[1].split(" - ")[1])
                        elif guncellenecek_indis == "4":
                            self.eser.yer_guncelle(secilen_eser[1].split(" - ")[1])                                                                                                                              
                    elif secilen_eser[0] == "Makale":  
                        self.eser = icerikler[2](secilen_eser[1].split(" - ")[0] ,secilen_eser[1].split(" - ")[1] ,secilen_eser[1].split(" - ")[2] ,secilen_eser[1].split(" - ")[3] ,secilen_eser[1].split(" - ")[4] ,secilen_eser[1].split(" - ")[5] ,secilen_eser[1].split(" - ")[6] ,secilen_eser[1].split(" - ")[7])     
                        print("Eserde güncellemek istediğiniz şeyi giriniz: ")
                        print("1- Durum güncelle: ")
                        print("2- Dil güncelle: ")
                        guncellenecek_indis = input("Seçiminiz: ")
                        if guncellenecek_indis == "1":
                            self.eser.durum_guncelle(secilen_eser[1].split(" - ")[1]) 
                        elif guncellenecek_indis == "2":
                            self.eser.dil_guncelle(secilen_eser[1].split(" - ")[1])               
            elif seciminiz == "10":
                print("Çıkış yapılıyor.")
                self.nesne = None
                self.eser = None
                self.giris_ekrani()
            else:
                print("Geçerli bir sayı giriniz: ")
    
        

    def giris_ekrani(self):
        while True:
            print("1- Kayıt Yap: ")
            print("2- Giriş Yap: ")
            print("3- Çıkış Yap: ")
            secim = input("Yapmak istediğiniz işlemi seçiniz: ")
            if secim == "1":
                ad = input("Adınız: ")
                soyad = input("Soyadınız: ")
                k_ad = input("Kullanıcı Adınız: ")
                sifre = input("Şifreniz: ") 
                with open("hesaplar.txt", "r", encoding="utf-8") as dosya:
                    mevcut_veriler = dosya.readlines()
                for satir in mevcut_veriler:
                    if k_ad in satir.split():
                        print("Bu kullanıcı adı zaten var!")
                        return
                else:
                    self.nesne = self.hesaplar[0](ad, soyad, k_ad, sifre)
                    self.nesne.kayit_ol()
            elif secim == "2":
                k_ad = input("Kullanıcı Adınız: ")
                sifre = input("Şifreniz: ")                
                with open("hesaplar.txt", "r", encoding="utf-8") as dosya:
                    mevcut_veriler = dosya.readlines()

                # Her satırda verileri kontrol et
                for satir in mevcut_veriler:
                    parcalar = satir.strip().split(" - ")

                    # Eğer satırda beklenmeyen eksik veriler varsa, bu satırı atla
                    if len(parcalar) < 5:
                        continue  # Hatalı satırı atla
                    ad = parcalar[0].strip()
                    soyad = parcalar[1].strip()
                    mevcut_k_ad = parcalar[2].strip()
                    mevcut_sifre = parcalar[3].strip()
                    hesap_turu = parcalar[4].strip()
                    if k_ad == mevcut_k_ad and sifre == mevcut_sifre:
                        print(f"Giriş başarılı! Hoşgeldiniz, {ad} {soyad} - {hesap_turu}.")

                        if hesap_turu == "uye":
                            self.nesne = self.hesaplar[0](ad, soyad, k_ad, sifre)
                            self.icerik(self.hesaplar, self.icerikler)
                        elif hesap_turu == "yazar":
                            self.nesne = self.hesaplar[1](ad, soyad, k_ad, sifre)
                            self.icerik(self.hesaplar, self.icerikler)
                        elif hesap_turu == "moderator":
                            self.nesne = self.hesaplar[2](ad, soyad, k_ad, sifre)
                            self.icerik(self.hesaplar, self.icerikler)
                        else:
                            print("Hesap türü hatalı.")
                            return
                        break
                else:
                    print("Kullanıcı adı veya şifre hatalı.")
            elif secim == "3":
                print("Çıkış Yapılıyor...")
                sys.exit()
            else:
                print("Geçerli bir sayı giriniz: ")    