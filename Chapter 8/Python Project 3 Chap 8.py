listA= []
banyak= int(input("Masukkan Jumlah Mahasiswa= "))

x = 0
for x in range (0,banyak):
    x += 1
    nama = str(input("Masukan nama mahasiswa ke-"+ str(x) + " = "))
    a = 0
    for x in nama :
        a += 1
    karakter = nama + "(" + str(a) + " karakter)"
    listA.append(karakter)

#hasil urutan abjad
print("Pendataan nama mahasiswa")
listA.sort()
for y in listA:
    print(y)
