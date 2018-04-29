def kaprekar(sayi):
    sayiStr = str(sayi)
    uzunluk = len(sayiStr)
    sayi1 = 0
    sayi2 = 0
    sayiTemp = 0
    if uzunluk % 2 == 0:
        sayiTemp = sayi**sayi
        print(int(sayiStr[:uzunluk]))
        sayi1 = int(sayiStr[:uzunluk])
        sayi2 = int(sayiStr[uzunluk:])
        sayiTemp = sayi1 + sayi2
        if sayiTemp == sayi:
            return 1
        else:
            return 0

print(kaprekar(5))