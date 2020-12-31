while True:
    try:
        buka = open("d:\Maulia Project 2.txt", "a+")
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama Mahasiswa: ")
        almt = input("Masukkan Alamat: ")
        ulang = input("Lagi? (y/n): ")
        if ulang == "n":
            x = nim + "|" + nama + "|" + almt + "\n"
            buka.write(x)
            buka.close()

            buka = open("d:\Maulia Project 2.txt", "r")
            print("Rincian isi file Maulia Project 2: ")
            cek = buka.read()
            print(cek)
            break
        if ulang == "y":
            x = nim + "|" + nama + "|" + almt + "\n"
            buka.write(x)
            buka.close()
            continue
        else:
            print("Ysng ksmu masukkan salah")
    except ValueError:
        print("Yang kamu masukkan salah")
