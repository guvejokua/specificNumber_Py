def kontrol(x):
    sayiStr = str(x)
    esit = 0
    for i in range(0, len(sayiStr), 1):
        esit = esit + (int(sayiStr[i])) ** len(sayiStr)
    if esit == x:
        return 1
    else:
        return 0
enBuyuk = 0
for j in range(1, 100000, 1):
    if kontrol(j):
        print("Bir Amstron Sayısı Bulundu = {}\n".format(j))
        if j > enBuyuk:
            enBuyuk = j
print(enBuyuk)
input()
