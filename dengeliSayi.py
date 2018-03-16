def ciftMi(x):
    if int(x % 2) == 0:
        return 1
    else:
        return 0


def tekMi(k):
    if int(k % 2) != 0:
        return 1
    else:
        return 0


def dengeliMi(sayi1):
    sayi = str(sayi1)
    if sayi[0] != sayi[1] != sayi[2] != sayi[3]:
        if ciftMi(int(sayi[0])) == 1 & ciftMi(int(sayi[1])) == 1 & tekMi(int(sayi[2])) == 1 & tekMi(int(sayi[3])) == 1:
            return 1
        elif tekMi(int(sayi[0])) == 1 & tekMi(int(sayi[1])) == 1 & ciftMi(int(sayi[2])) == 1 & ciftMi(int(sayi[3])) == 1:
            return 1
        else:
            return 0
    else: return 0

toplam = 0
for i in range(1000, 10000, 1):
    if dengeliMi(i):
        toplam = toplam + 1
    print("Sayı = {} Dengelilik = {}".format(i, dengeliMi(i)))

print(toplam)
input()
