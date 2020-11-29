print("Dsftar harga buah per kilogram: ")
daftar ={"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" :6500}

x=0
for a,b in daftar.items():
    x+=1
    print(x, ".", a, "=", b)
jumlah=0
while True:
    nama = input("Nama buah yang dibeli  = ")
    if(nama in daftar):
        kg= float(input("Berapa Kg              = "))
        print("_____________________________")
        jumlah+= (daftar[nama]*kg)
        pil= str(input("Beli buah yang lain (y/n)? "))
        if pil=="n":
            print("Total harga: ", jumlah)
            break
    else:
        print(nama, "tidak terdapat di daftar buah")
        
       
        


