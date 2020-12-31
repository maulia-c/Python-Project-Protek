def dekripsi(a, b) :    
    listt = list(a)
    for x in range(len(listt)) :
        if(listt[x] != ' ') :
            if(ord(listt[x]) - b >= 65) :
                asci = ord(listt[x])
                desc = asci - b
                listt[x] = chr(desc)
            else :
                asci = ord(listt[x])
                desc = (asci + 26) - b
                listt[x] = chr(desc)
        else :
            continue
    result = ''.join(listt)
    return result

try :    
    teks = input("Masukkan teks yang akan di dekripsi : ")
    enkr = int(input("Jumlah geseran dekripsi : "))
    hasil = dekripsi(teks, enkr)
    print("\nHasil pengenkripsian teks {0} adalah : {1}".format(teks, hasil))
except ValueError :
    print("Masukkan bilangan bulat")
