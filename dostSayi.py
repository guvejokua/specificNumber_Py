def pozitifBolenler(sayi):
    bolenlerToplami = 0
    for i in range(1, sayi, 1):
        if sayi % i == 0:
            bolenlerToplami = bolenlerToplami + i
    print("Bolenleri toplamı {}".format(bolenlerToplami))
    return bolenlerToplami

def dostMu(a):
    if a == pozitifBolenler(pozitifBolenler(a)):
        return 1
    else: return 0

toplamDost = 0
for j in range(1, 10000, 1):
    if dostMu(j):
        toplamDost = toplamDost + 1
        print("Dost Sayı bulundu {} ile {}\n".format(j, pozitifBolenler(j)))
print("Toplam Dost Sayı sayısı {}".format(toplamDost))

print(pozitifBolenler(496))