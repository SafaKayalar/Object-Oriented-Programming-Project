from Sistem import menu
from Sistem.Hesaplar.Moderator import moderator
from Sistem.Hesaplar.Yazar import icerik_ureticisi
from Sistem.Hesaplar.Uye import uye
from Sistem.içerikler.Dergi import dergi
from Sistem.içerikler.Konferans import konferans
from Sistem.içerikler.Makale import makale

if __name__ == "__main__":

    hesaplar = [uye, icerik_ureticisi, moderator]
    icerikler = [dergi,konferans,makale]
    menu = menu(hesaplar,icerikler)
    menu.giris_ekrani()