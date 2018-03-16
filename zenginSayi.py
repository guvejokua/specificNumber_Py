def bolenleri(x):
    bolenler = 0
    for i in range(1, x, 1):
        if x % i == 0:
            bolenler = bolenler + i

    if bolenler > x:
        return 1
    else:
        return 0
toplam = 0
for j in range(1, 100000, 1):
    if bolenleri(j):
        print("{} sayısı bir zengin sayıdır \n".format(j))
        toplam = toplam + 1
print(toplam)
input()
