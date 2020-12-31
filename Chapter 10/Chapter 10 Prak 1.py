file = open("d:\Maulia,txt", "w")
file.write("100\n102\n99\n89\n192\n938\n107\n241\n")
file.close()

file = open("d:\Maulia.txt", "r")
baris = file.readlines()

x = 0
gnp = 0
gjl = 0

try:
    while True:
        isi = int(baris[x])
        if isi % 2 == 0:
            gnp += 1
        if isi % 2 == 1:
            gjl += 1
        x += 1

        if not baris:
            break
except:
    print("Jumlahnya ")
print ("Genap: ",gnp)
print ("Ganjil: ",gjl)
