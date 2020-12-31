buka = open("d:\Maulia Project 2.txt", "r")
isi1 = []
isi2 = []
isi3 = []
for baris in buka:
    ubah = baris.split("|")
    isi1.append(ubah[0])
    isi2.append(ubah[1])
    isi3.append(ubah[2].strip())
cari = str(input("Masukkan NIM yang akan dicari: "))
if cari in isi1:
    x = isi1.index(cari)
    print("Data Mahasiswa","\nNIM: ",isi1[x],"\nNama: ",isi2[x],"\nAlamat: ",isi3[x]) 
else:
    print("Data Tidak Ditemukan")
    
