import random
huruf = str(input("Masukkan kata yang ingin diulangi = "))
jumlah= int(input("Masukkan banyak percobaan pengulangan = "))


def sufflestring(k,x):
    text = list(k)
    lis = []
    for i in range(x):
        random.shuffle(text)
        a = ("".join(text))
        if a not in lis:
            lis.append(a)
    print(lis)

sufflestring(huruf, jumlah)
