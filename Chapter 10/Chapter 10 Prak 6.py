def enkripsi(a, b) :
    listt = list(a)
    for x in range(len(listt)) :
        if(listt[x] != " ") :
            if(ord(listt[x]) + b < 91) :
                ascii = ord(listt[x])
                y = ascii + b
                listt[x] = chr(y)
            else :
                ascii = ord(listt[x])
                y = (ascii + b) - 26
                listt[x] = chr(y)
        else :
            continue
    hasil = "".join(listt)
    return hasil
try :
    masuk = input("File yang akan di enkripsi (contoh(d:/___.txt)): ")
    file = open(masuk,"r")
    baca = (file.read())
    jmlh = int(input("Jumlah enkripsi : "))
    hasil = enkripsi(baca, jmlh)
    sandi = open("d:/sandiacak.txt","a")
    sandi.write(hasil)
    sandi.close()
    print("\nHasil pengenkripsian teks {0} adalah : {1}".format(baca, hasil),
          ("\n\n\tHasilnya ini bisa  dilihat pada (d:/sandiacak.txt)"))
except ValueError :
    print("Masukkan Bilangan Bulat")


    
