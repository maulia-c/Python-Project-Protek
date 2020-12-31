buka = open("d:\Maulia Project 2.txt", "r")
baris = buka.readlines()
buka = len(baris)
make = {}
x=0
for text in range(0,buka):
        a = baris[x]
        ubah = a.split("|")
        a = ubah[0]
        b = ubah[1]
        c = ubah[2].replace("\n", "")
        x+=1
        hasil = {"nim":a,"name":b,"alamat":c}
        susunan = {x : hasil}
        make.update(susunan)
print(make)
