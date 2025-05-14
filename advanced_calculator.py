import math
print("Gelişmiş Hesap Makinesi")

while True:
    print("\nİşlemler:")
    print("1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")
    print("5 - Üs Alma")
    print("6 - Karekök Alma")
    print("7 - Mod Alma")
    print("0 - Çıkış")

    secim = input("Bir işlem seçin (0-7): ")

    if secim == "0":
        print("Çıkılıyor...")
        break

    if secim == "1":
        a = float(input("1.sayı: "))
        b = float(input("2.sayı: "))
        def toplama(x,y):
            return x + y
        print("Sonuç:",toplama(a,b))

    elif secim == "2":
        a = float(input("1.sayı: "))
        b = float(input("2.sayı: "))
        def cıkarma(x,y):
            return x - y
        print("Sonuç:", cıkarma(a,b))

    elif secim == "3":
        a = float(input("1.sayı: "))
        b = float(input("2.sayı: "))
        def carpma(x,y):
            return x * y
        print("Sonuç:", carpma(a,b))

    elif secim == "4":
        a = float(input("1. sayı: "))
        b = float(input("2. sayı: "))
        def bolme(x,y):
            if y == 0:
                return "Hata.Sıfıra bölünemez!"
            return x / y
        print("Sonuç:", bolme(a,b))

    elif secim == "5":
        a = float(input("Taban sayıyı girin: "))
        b = float(input("Üssü girin: "))
        def us_alma(x,y):
            return x ** y
        print("Sonuç:", us_alma(a,b))

    elif secim == "6":
        a = float(input("Karekökünü almak istediğiniz sayıyı girin: "))
        def karekok(x):
            if x < 0:
                return "Negatif sayının karekökü alınmaz !"
            return math.sqrt(x)
        print("Sonuç:", karekok(a))

    elif secim == "7":
        a = float(input("1. sayı: "))
        b = float(input("2. sayı: "))
        def mod_alma(x,y):
            return x % y
        print("Sonuç:", mod_alma(a,b))

    else:
        print("Geçersiz sayı! Lütfen geçerli bir işlem numarası girin.")


