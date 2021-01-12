import datetime
while True:
    code = input("Masukkan Kode Member  = ")
    name = input("Masukkan Nama Member	= ")
    jdl = input("Masukkan Judul Buku   = ")

    print("\n")
    lagi = input("Ulangi lagi (y/n) = ")
    print("\n")

    if lagi == "n":
        skrg = datetime.date.today()
        slsai = datetime.timedelta(days=7)
        wktu = str(skrg + slsai)
        hari = str(skrg)
        buka = open("d:/maulia project 11.txt", "a+")
        buka.write(code + "|" + name + "|" + jdl + "|" + hari + "|" + wktu + "\n")
        buka.close
        buka = open("d:/maulia project 11.txt", "r")
        print("Data peminjam :")
        print(buka.read())
        buka.close()
        break
    elif lagi == "y":
        skrg = datetime.date.today()
        slsai = datetime.timedelta(days=7)
        wktu = str(skrg + slsai)
        hari = str(skrg)
        buka = open("d:/maulia project 11.txt", "a+")
        buka.write(code + "|" + name + "|" + jdl + "|" + hari + "|" + wktu + "\n")
        buka.close
        continue
    else:
        print("input anda salah")
        exit()
