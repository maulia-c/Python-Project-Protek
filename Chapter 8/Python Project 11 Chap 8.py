buah ={"apel" : 5000,
         "jeruk": 8500,
         "mangga":7800,
         "duku" : 6500}
while True:
    listA= ["Menu:",
    "A. Tambah data buah",
    "B. Beli buah",
    "C. Tampilkan data buah",
    "D. Tutup program"]

    for c in listA:
        print(c)
    print("Data buah: ", buah)
    menu = str(input("Pilihan anda (A/B/C/D) = "))


    if menu == "A":
        while True:
            tambahan = str(input("nama buah yang ingin ditambahakan = "))
            if tambahan in buah:
                print("buah", tambahan, "sudah terdapat di data")
            
            else:
                harga= int(input("Harga buah= "))
                buah.update({tambahan:harga})
                print("perubahan data buah = ", buah)
                lagi= str(input("Mau menambahkan lagi(y/n)? "))
                if lagi == "y":
                    print("perubahan data buah = ", buah)
                elif lagi== "n":
                    break
    
    elif menu == "B":
        jumlah=0
        while True:
            nama = str(input("Nama buah yang dibeli  = "))
            if nama in buah:
                kg= float(input("Berapa Kg= "))
                jumlah+= (buah[nama]*kg)
                pil= str(input("Beli buah yang lain (y/n)? "))
                if pil=="n":
                    print("Total harga: ", jumlah)
                    break
            else:
                print(nama, "tidak terdapat di daftar buah")
    elif menu == "C":
        for a,b in buah.items():
            print("harga ",a ," = ", b)
    elif menu== "D":
        print("Terima kasih atas kunjungan anda")
        break
    else:
        print("tidak ditemukan")
    
