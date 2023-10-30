#Efe Öztaş
#Başar Burak Ünal


from colorama import Fore, Style, init


init(autoreset=True)

while True:
    print(Fore.LIGHTCYAN_EX + "Problem Menüsü:")
    print(Fore.LIGHTYELLOW_EX + "\n1. Problem -> K’nıncı En Küçük Elemanı Bulma")
    print(Fore.LIGHTMAGENTA_EX + "\n2. Problem -> En Yakın Çifti Bulma")
    print(Fore.LIGHTGREEN_EX + "\n3. Problem -> Bir Listenin Tekrar Eden Elemanlarını Bulma")
    print(Fore.LIGHTRED_EX + "\n4. Problem -> Matris Çarpımı")
    print(Fore.LIGHTBLUE_EX + "\n5. Problem -> Bir Text Dosyasındaki Kelimelerin Frekansını Bulma")
    print(Fore.LIGHTYELLOW_EX + "\n6. Problem -> Liste İçinde En Küçük Değeri Bulma")
    print(Fore.LIGHTCYAN_EX + "\n7. Problem -> Karekök Fonksiyonu")
    print(Fore.LIGHTMAGENTA_EX + "\n8. Problem -> En Büyük Ortak Bölen")
    print(Fore.LIGHTGREEN_EX + "\n9. Problem -> Asallık Testi")
    print(Fore.LIGHTRED_EX + "\n10. Problem -> Daha Hızlı Fibonacci Hesabı")
    print(Fore.LIGHTWHITE_EX + "\n11 -> Çıkış")

    secim = input(Fore.LIGHTYELLOW_EX + "\nBir problem seçin (çıkış için 11 yazın): ")




    if secim == "11":
        print("Programdan çıkılıyor...")
        break
    elif secim == "1":
        def k_kucuk(k, liste):
            if k > 0 and k <= len(liste):
                liste.sort()
                k_nci_eleman = liste[k - 1]
                return k_nci_eleman
            else:
                return None

        while True:
            try:

                k = int(input("k değerini girin: "))
                if k <= 0:
                    print("Geçersiz k değeri. Lütfen 1 veya 1'den büyük bir değer girin.")
                    continue

                liste = input("Liste elemanlarını virgülle ayırıp girin: ").split(',')
                liste = [int(x.strip()) for x in liste]

                sonuc = k_kucuk(k, liste)
                if sonuc is not None:
                    print(k_kucuk(k, liste))
                else:
                    print("Geçersiz liste girişi,lütfen k değerini liste sayılarından az veya aynı girin.")
                break
            except ValueError:
                print("Geçersiz giriş,tekrar deneyin.")
        devam = input("Devam etmek için 'D' tuşuna, çıkmak için 'D' hariç herhangi bir tuşa basın: ")
        if devam.upper() != "D":
            break
        pass
    elif secim == "2":
        def en_yakin_cift(hedef, liste):
            if len(liste) < 2:
                return None

            liste.sort()
            en_yakin_cift = None
            en_az_fark = float('inf')

            for i in range(len(liste) - 1):
                for j in range(i + 1, len(liste)):
                    toplam = liste[i] + liste[j]
                    fark = abs(toplam - hedef)

                    if fark < en_az_fark:
                        en_az_fark = fark
                        en_yakin_cift = (liste[i], liste[j])

            return en_yakin_cift

        while True:
            try:
                hedef = int(input("Hedef değeri girin: "))
                if hedef < 0:
                    print("Hedef değeri pozitif olmalıdır.")
                    continue

                liste = input("Sayıları virgülle ayırarak girin: ").split(',')
                liste = [int(x) for x in liste]

                en_yakin_cift = en_yakin_cift(hedef, liste)
                if en_yakin_cift is not None:
                    print(en_yakin_cift[0], "ve", en_yakin_cift[1])
                else:
                    print("Listede en az iki sayı olmalıdır.")
                break
            except ValueError:
                print("Hatalı giriş! Lütfen geçerli sayılar girin.")
        devam = input("Devam etmek için 'D' tuşuna, çıkmak için 'D' hariç herhangi bir tuşa basın: ")
        if devam.upper() != "D":
            break
        pass
    elif secim == "3":
        def tekrar_eden_elemanlar(liste):
            tekrar_eden_elemanlar_sonuc = [x for x in liste if liste.count(x) > 1]
            return list(set(tekrar_eden_elemanlar_sonuc))

        while True:
            try:
                liste_girisi = input("Listeyi virgülle ayırarak girin: ")
                liste = [int(x.strip()) for x in liste_girisi.split(",")]

                sonuc = tekrar_eden_elemanlar(liste)
                if sonuc:
                    print(tekrar_eden_elemanlar(liste))
                else:
                    print("Tekrar eden eleman yok")
                break
            except ValueError:
                print("Geçersiz giriş,tekrar deneyin.")
        devam = input("Devam etmek için 'D' tuşuna, çıkmak için 'D' hariç herhangi bir tuşa basın: ")
        if devam.upper() != "D":
            break
        pass

    elif secim == "4":
        def matris_olustur(satir, sutun):
            matris = []
            for i in range(satir):
                satir_degerleri = []
                for j in range(sutun):
                    try:
                        deger = int(input("Matrisin (" + str(i + 1) + "," + str(j + 1) + ") elemanını girin: "))
                        satir_degerleri.append(deger)
                    except ValueError:
                        print("Geçersiz bir sayı girdiniz. Lütfen geçerli bir sayı girin.")
                        return None
                matris.append(satir_degerleri)
            return matris

        def matris_carpimi(matris1, matris2):
            m1_satir = len(matris1)
            m1_sutun = len(matris1[0])

            m2_satir = len(matris2)
            m2_sutun = len(matris2[0])

            if m1_sutun != m2_satir:
                return "Matris boyutları uyumsuz!"

            sonuc = [[0 for _ in range(m2_sutun)] for _ in range(m1_satir)]

            for i in range(m1_satir):
                for j in range(m2_sutun):
                    sonuc[i][j] = sum(a * b for a, b in zip(matris1[i], (matris2[k][j] for k in range(m1_sutun))))

            return sonuc

        while True:
            try:
                m1_satir = int(input("İlk matrisin satır sayısını girin: "))
                m1_sutun = int(input("İlk matrisin sütun sayısını girin: "))
                print("İlk matrisi girin:")
                matris1 = matris_olustur(m1_satir, m1_sutun)

                if matris1 is not None:
                    m2_satir = int(input("İkinci matrisin satır sayısını girin: "))
                    m2_sutun = int(input("İkinci matrisin sütun sayısını girin: "))
                    print("İkinci matrisi girin:")
                    matris2 = matris_olustur(m2_satir, m2_sutun)

                    if matris2 is not None:
                        sonuc = matris_carpimi(matris1, matris2)

                        if sonuc != "Matris boyutları uyumsuz!":
                            for satir in sonuc:
                                print(satir)
                        else:
                            print("Matris boyutları uyumsuz olduğu için çarpım yapılamamaktadır.")
                        break
            except ValueError:
                print("Geçersiz bir sayı girdiniz. Lütfen tekrar deneyin.")
        devam = input("Devam etmek için 'D' tuşuna, çıkmak için 'D' hariç herhangi bir tuşa basın: ")
        if devam.upper() != "D":
            break
        pass
    elif secim == "5":
        from functools import reduce

        def kelime_frekansi(dosya_adi):
            try:
                with open(dosya_adi, 'r') as dosya:
                    kelimeler = dosya.read().split()

                kelime_frekanslari = reduce(
                    lambda acc, kelime: {**acc, kelime: acc.get(kelime, 0) + 1},
                    map(lambda kelime: kelime, kelimeler),
                    {})

                return kelime_frekanslari

            except FileNotFoundError:
                return None

        dosya_adi = input("Dosya adını girin: ")
        sonuc = kelime_frekansi(dosya_adi)

        if sonuc is not None:
            for kelime in sonuc.keys():
                frekans = sonuc[kelime]
                print(f"{kelime}={frekans}")
        else:
            print("Dosya bulunamadı.")
        devam = input("Devam etmek için 'D' tuşuna, çıkmak için 'D' hariç herhangi bir tuşa basın: ")
        if devam.upper() != "D":
            break
        pass
    elif secim == "6":
        def en_kucuk_deger(liste):
            if len(liste) == 1:
                return liste[0]

            ilk_eleman = liste[0]
            kalan_liste = liste[1:]
            en_kucuk_kalan = en_kucuk_deger(kalan_liste)

            if ilk_eleman < en_kucuk_kalan:
                return ilk_eleman
            else:
                return en_kucuk_kalan

        while True:
            try:
                liste_girisi = input("Listedeki sayıları virgül ile ayırıp giriniz: ")
                liste = [int(x) for x in liste_girisi.split(',')]
                en_kucuk = en_kucuk_deger(liste)
                print(en_kucuk_deger(liste))
                break
            except ValueError:
                print("Geçersiz giriş,tekrar deneyin.")
        devam = input("Devam etmek için 'D' tuşuna, çıkmak için 'D' hariç herhangi bir tuşa basın: ")
        if devam.upper() != "D":
            break
        pass
    elif secim == "7":
        def hata_toleransa_uzaklik(hata, tol):
            uzaklik = abs(hata - tol)
            if uzaklik < tol:
                return f"Hata toleransı olan {tol} kadar yaklaşıldı. Hata: {hata:.10f}, Tolerans: {tol:.10f}"
            else:
                return f"Hata toleransından {uzaklik:.10f} kadar uzak. Hata: {hata:.10f}, Tolerans: {tol:.10f}"

        def babil_karekok(N, x0, tol=1e-10, maxiter=10):
            for i in range(maxiter):
                try:
                    x1 = 0.5 * (x0 + N / x0)
                except ZeroDivisionError:
                    print("Sıfıra bölme hatası. İlk tahmin (x0) sıfır olamaz.")
                    return None
                hata = abs(x1 ** 2 - N)

                uyari_mesaji = hata_toleransa_uzaklik(hata, tol)
                print("Iterasyon", i + 1, uyari_mesaji)

                if hata < tol:
                    return x1
                x0 = x1

            print(maxiter, "iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirin")
            x1 = x0
            return x1

        try:
            N = float(input("Karekökünü almak istediğiniz sayıyı (N) giriniz: "))
            x0 = float(input("İlk tahmini (x0) giriniz: "))
            maxiter = int(input("Azami iterasyon sayısını (maxiter) giriniz: "))
        except ValueError:
            print("Geçersiz giriş. Lütfen sayısal değerler girin.")
        else:

            sonuc = babil_karekok(N, x0, maxiter=maxiter)
            if sonuc is not None:
                print(sonuc)
        devam = input("Devam etmek için 'D' tuşuna, çıkmak için 'D' hariç herhangi bir tuşa basın: ")
        if devam.upper() != "D":
            break
        pass
    elif secim == "8":
        def eb_ortak_bolen(sayi1, sayi2):
            if sayi2 == 0:
                return sayi1
            else:
                return eb_ortak_bolen(sayi2, sayi1 % sayi2)

        while True:
            try:
                sayi1 = int(input("Birinci sayıyı giriniz: "))
                sayi2 = int(input("İkinci sayıyı giriniz: "))

                print(eb_ortak_bolen(sayi1, sayi2))
                break
            except ValueError:
                print("Hatalı giriş,tekrar deneyin.")
        devam = input("Devam etmek için 'D' tuşuna, çıkmak için 'D' hariç herhangi bir tuşa basın: ")
        if devam.upper() != "D":
            break
        pass
    elif secim == "9":
        def asal_veya_degil(sayi):

            if sayi <= 1:
                return False

            elif sayi == 2:
                return True

            elif sayi % 2 == 0:
                return False

            else:
                return bolunebilirlik(sayi, 3)

        def bolunebilirlik(sayi, bolen):

            if bolen * bolen > sayi:
                return True

            elif sayi % bolen == 0:
                return False

            else:
                return bolunebilirlik(sayi, bolen + 2)

        try:
            sayi = int(input("Sayı girin: "))
            sonuc = asal_veya_degil(sayi)

            if sonuc:
                print(asal_veya_degil(sayi))
            else:
                print(asal_veya_degil(sayi))

        except ValueError:
            print("Geçersiz bir sayı girdiniz. Lütfen bir tam sayı girin.")
        devam = input("Devam etmek için 'D' tuşuna, çıkmak için 'D' hariç herhangi bir tuşa basın: ")
        if devam.upper() != "D":
            break
        pass
    elif secim == "10":
        def hizlandirici(n, k, fibk, fibk1):
            print(n, k, fibk, fibk1)
            if n == k:
                return fibk
            else:
                return hizlandirici(n, k + 1, fibk + fibk1, fibk)

        try:
            n = int(input("Hesaplanacak Fibonacci sayısının sırasını girin: "))
            k = int(input("Başlangıç sırasını girin: "))
            fibk = int(input("Başlangıç sırasındaki Fibonacci sayısını girin: "))
            fibk1 = int(input("Başlangıçtan bir önceki sıradaki Fibonacci sayısını girin: "))
        except ValueError:
            print("Lütfen sayısal bir değer girin.")
        else:
            if n < 0 or k < 0 or fibk < 0 or fibk1 < 0:
                print("Lütfen pozitif bir sayı girin.")
            else:
                try:
                    hizlandirici(n, k, fibk, fibk1)
                except IndexError:
                    print("Lütfen geçerli bir Fibonacci sırası girin.")
        devam = input("Devam etmek için 'D' tuşuna, çıkmak için 'D' hariç herhangi bir tuşa basın: ")
        if devam.upper() != "D":
            break
        pass
    else:
        print("Geçersiz seçim. Lütfen geçerli bir seçenek girin.")
        devam = input("Devam etmek için 'D' tuşuna, çıkmak için 'D' hariç herhangi bir tuşa basın: ")
        if devam.upper() != "D":
            break
        pass
