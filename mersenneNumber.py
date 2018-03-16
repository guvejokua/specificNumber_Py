def asal(x):
    for i in range(2, x, 1):
        if x % i == 0:
            return 0
    return 1

toplam = 0

for k in range(2, 20, 1):
    sayi = 2**k - 1
    if sayi > 100000: break
    if asal(sayi):
        toplam = toplam + 1
        print("Bir Mersenne ve asal sayı bulundu {}\n".format(sayi))
print(toplam)
