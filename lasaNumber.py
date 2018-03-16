def asal(x):
    for i in range(2, x, 1):
        if x % i == 0:
            return 0
    return 1

def re(y):
    strin = str(y)
    strin = strin[::-1]
    return int(strin)

toplam = 0
for j in range(2, 100000, 1):
    if asal(j):
        if asal(re(j)):
            toplam = toplam + 1
            print("Bir lasa sayısı bulundu {}\n".format(j))
print(toplam)

