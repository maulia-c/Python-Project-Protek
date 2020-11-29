print("Dsftar harga buah per kilogram: ")
daftar ={"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" :6500}

y = 0
for a,b in daftar.items():
    y += 1
    print(y ,".", a ,"=",b)

nama = input("Nama buah yang dibeli  = ")
if(nama in daftar):
    kg= float(input("Berapa Kg              = "))
    print("_____________________________")
    print("Total harga           :",daftar[nama]*kg)
else:
    print(nama, "tidak terdapat di daftar buah")
