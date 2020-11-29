nama= input("Masukkan nama file (d:/anyfiles.txt): ")
try:
    file = open(nama, "r")
    x= "y"
    while x== "y":
        file= open(nama, "a")
        tambah= input("Data yang mau ditambahkan: " )
        file.write(tambah)
        lagi= input("Mau Lagi (y/n): ")
        file.close
        if lagi != "y":
            break
except FileNotFoundError:
    print("Input tidak valid")

            
    




