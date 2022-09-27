import time
import random

print("Bankaya Hoşgeldiniz.")
hesap = {
        "ad": input("Adınız: "),
        "soyad": input("Soyadınız: "),
        "kartSifre": int(input("Bir şifre Belirleyiniz: ")),
        "hesapNo": int(random.randint(120, 220)),
        "bakiye": int(random.randint(6471, 12942))
    }
def sistem(hesap):
        while True:
            secim = int(input("\n1- Bakiye\n2- Hesap Bilgileri\n3- Para Çek\n4- Para Yatır\n5- Para Gönder\n6- Faturaları Öde\n7- Faturaları Gör\nSeçin Yapınız: "))
            if secim == 1:
                print("\nBakiyeniz: {}\n".format(hesap["bakiye"]))
            if secim == 2:
                print("\n",hesap,"\n")
            if secim == 3:
                paraCek = int(input("Tutar: "))
                if paraCek > hesap["bakiye"]:
                    print("Yeterli miktarda paranız yok.")
                if paraCek < hesap["bakiye"]:
                    print("\nPara Çekildi.\n")
                    hesap["bakiye"] -= paraCek
            if secim == 4:
                paraYatir = int(input("Tutar: "))
                print("\nPara Yatırıldı.")
                hesap["bakiye"] += paraYatir
            if secim == 5:
                print("Not: Gönderilecek Kişi Dolduracaktır!\n")
                gonderHesap = {
                    "ad": input("Adınız: "),
                    "soyad": input("Soyadınız: "),
                    "kartSifre": int(input("Bir şifre Belirleyiniz: ")),
                    "hesapNo": int(random.randint(120, 220)),
                    "bakiye": int(6471)
                }
                paraGonder = int(input("\nGönderilecek Tutar: "))
                if paraGonder > hesap["bakiye"]:
                    print("\nYeterli miktarda paranız yok.\n")
                if paraGonder < hesap["bakiye"]:
                    randomDeger = random.randint(1, 3)
                    if randomDeger == 2:
                        print("Para Gönderilemedi.")
                    if randomDeger == 1 or randomDeger == 3:
                        print("\nPara Gönderildi.\n")
                        hesap["bakiye"] -= paraGonder
                        gonderHesap["bakiye"] += paraGonder
            if secim == 6:
                faturalar = {
                    "suFaturası": int(random.randint(250, 750)),
                    "dogalgazFaturası": int(random.randint(750, 1750)),
                    "elektrikFaturası": int(random.randint(180, 250)),
                    "internetFaturası": int(random.randint(500, 1750))
                }
                faturaSecim = int(input("1- Su Faturası'nı Öde\n2- Elektrik Faturası'nı Öde\n3- Doğalgaz Faturası'nı Öde\n4- İnternet Faturası'nı Öde\n Seçim Yapınız: "))
                if faturaSecim == 1:
                    if faturalar["suFaturası"] > hesap["bakiye"]:
                        print("Ödeyecek Paranız Yok.")
                    if faturalar["suFaturası"] < hesap["bakiye"]:
                        SuFaturaTutar = int(input("Tutar: "))
                        print("Fatura Ödendi.")
                        faturalar["suFaturası"] -= SuFaturaTutar
                    if SuFaturaTutar > faturalar["suFaturası"]:
                            print("Fazla Değer Girdiniz. Su Faturanız: {} TL'dir.".format(faturalar["suFaturası"]))
                if faturaSecim == 2:
                    if faturalar["elektrikFaturası"] > hesap["bakiye"]:
                        print("Ödeyecek Paranız Yok.")
                    if faturalar["elektrikFaturası"] < hesap["bakiye"]:
                        ElektrikFaturaTutar = int(input("Tutar: "))
                        print("Fatura Ödendi.")
                        faturalar["suFaturası"] -= ElektrikFaturaTutar
                    if ElektrikFaturaTutar > faturalar["elektrikFaturası"]:
                            print("Fazla Değer Girdiniz. Elektrik Faturanız: {} TL'dir.".format(faturalar["elektrikFaturası"]))
                if faturaSecim == 3:
                    if faturalar["dogalgazFaturası"] > hesap["bakiye"]:
                        print("Ödeyecek Paranız Yok.")
                    if faturalar["dogalgazFaturası"] < hesap["bakiye"]:
                        DogalgazFaturaTutar = int(input("Tutar: "))
                        print("Fatura Ödendi.")
                        faturalar["dogalgazFaturası"] -= DogalgazFaturaTutar
                    if DogalgazFaturaTutar > faturalar["dogalgazFaturası"]:
                            print("Fazla Değer Girdiniz. Doğalgaz Faturanız: {} TL'dir.".format(faturalar["dogalgazFaturası"]))
                if secim == 4:
                    if faturalar["internetFaturası"] > hesap["bakiye"]:
                        print("Ödeyecek Paranız Yok.")
                    if faturalar["internetFaturası"] < hesap["bakiye"]:
                        internetFaturaTutar = int(input("Tutar: "))
                        print("Fatura Ödendi.")
                        faturalar["internetFaturası"] -= internetFaturaTutar
                    if internetFaturaTutar > faturalar["internetFaturası"]:
                            print("Fazla Değer Girdiniz. İnternet Faturanız: {} TL'dir.".format(faturalar["internetFaturası"]))
            if secim == 7:
                print("\n",faturalar,"\n")

# Login ------------------------------------------ Login #

giris = int(input("Giriş Yapmak için; Kart Şifre:"))
if giris == hesap["kartSifre"]:
  print("Giriş Başarılı Sisteme Yönlendiriliyosunuz...")
  sistem(hesap)
else:
  print("Kart Şifresi Hatalı")
