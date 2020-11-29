sayur = ["bayam", "kangkung", "wortel", "selada"]
while True:
    listA= ["Menu:",
    "A. Tambah data sayur",
    "B. Hapus data sayur",
    "C. Tampilkan data sayur",
    "D. Berhenti",
    "Daftar Sayur Anda (bayam, kangkung, wortel, selada)"]

    for c in listA:
        print(c)

    
    menu = str(input("pilihan anda (A/B/C/D) = "))

    if menu == "A":
        tambahan = str(input("nama sayur yang ingin ditambahakan = "))
        if tambahan in sayur:
            print("Sayur sudah tersedia")
        else:
            sayur.append(tambahan)
            print("perubahan data sayur = ", sayur)
        
    elif menu == "B":
        try:
            hapus = str(input("nama sayur yang ingin dihapus = "))
            sayur.remove(hapus)
            print("Daftar sayur= ", sayur)
        except ValueError:
            print("data tidak ditemukan")
    elif menu == "C":
        print("Daftar sayur anda= ", sayur)
    elif menu=="D":
        print("Terimakasih")
        break
    else:
        print("tidak ditemukan")
