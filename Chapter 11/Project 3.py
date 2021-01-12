import datetime
buka = open("d:/maulia project 11.txt", "r")
data  = []
data2 = []
data3 = []
data4 = []
data5 = []

for line in buka:
    ubah = line.split("|")
    data.append(ubah[0])
    data2.append(ubah[1])
    data3.append(ubah[2])
    data4.append(ubah[3])
    data5.append(ubah[4].strip())

lagi = str(input("Masukkan kode member yang mau dicari : "))
if lagi in data:
    find = True
    a = data.index(lagi)
    NOW = datetime.datetime.now()
    x = data5[a]
    from datetime import datetime
    x = datetime.strptime(x, "%Y-%m-%d")
    rumus = x - NOW
    from datetime import *
    kembali = datetime.date(NOW)
    maks = datetime.date(x)
else:
    print("data tidak ditemukan")
    exit()
if find == True:
    rumus = datetime.date(NOW) - maks
    rumus = int(rumus.days)
    denda = 0
    if rumus >= 0:
        denda = 2000 *(rumus)
        rumus = abs(rumus)
    elif rumus <= 0:
        rumus = 0

    print("\nData Peminjaman Buku\n"
         "\nKode Member                    : ",data[a],
         "\nNama Member                    : ",data2[a],
         "\nJudul Buku                     : ",data3[a],
         "\nTanggal Mulai Peminjaman       : ",data4[a],
         "\nTanggal Maks Peminjaman        : ",data5[a],
         "\nTanggal Pengembalian           : ",kembali,
         "\ntelat                          : ", rumus,"Hari"
         "\nTotal denda                    :  Rp.",denda)

else:
    print("data tidak ditemukan")


