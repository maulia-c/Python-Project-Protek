buka = open("d:\Maulia Project 5.txt", "r")
a = buka.read()
buka.close()

buka = open("d:\Maulia Project 5.txt", "r")
baris = buka.readlines()
hasil = open("d:\Maulia Project Hasil 5.txt", "w")
for x in baris:
    isi = x.split("|")
    jumlah = int(isi[0]) + int(isi[1])
    hasil.write(str(jumlah))
    hasil.write("\n")
    print(isi)
buka.close()
hasil.close()

buka = open("d:\Maulia Project Hasil 5.txt", "r")
print(buka.read())
buka.close()
