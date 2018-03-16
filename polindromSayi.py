def kontrol(sayi):
    sayiString = str(sayi)
    yeniSayiString = sayiString
    yeniSayiString = sayiString[::-1]
    if int(yeniSayiString) == int(sayiString):
        return 1
    else:
        return 0
def onucBolum(x):
    if x % 13 == 0:
        return 1
    else:
        return 0
toplam = 0
for i in range(100000, 1000000, 1):
    if kontrol(i):
        print("Polindrom sayı = {}\n".format(i))
        if onucBolum(i):
            print("Hem Polindrom Hem de 13'e tam bölünen sayı = {}\n".format(i))
            toplam = toplam + 1

print("Toplam {}".format(toplam))
input()