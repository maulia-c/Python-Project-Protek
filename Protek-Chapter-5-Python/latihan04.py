kodeKaryawan= int(input("Masukkan kode Karyawan : "))
namaKaryawan= str(input("Masukkan Nama Karyawan : "))
golonganKaryawan= str(input("Masukkan Golongan  : "))

if(golonganKaryawan == "A"):
    gajiPokok= 10000000
    potongan= 2.5
elif(golonganKaryawan== "B"):
    gajiPokok= 8500000
    potongan= 2.0
elif(golonganKaryawan== "C"):
    gajiPokok= 7000000
    potongan= 1.5
elif(golonganKaryawan== "D"):
    gajiPokok= 5500000
    potongan= 1.0
else:
    print("Golongan Anda Tidak Ditemukan")
    exit()
    
#HitungPotonganGaji
PotonganGaji= gajiPokok*(potongan/100)

#TampilanHasilGaji
print("================Struk Gaji Karyawan==================")
print("Nama Karyawan; ",namaKaryawan)
print("Kode Karyawan: ",kodeKaryawan)
print("Golongan:  ",golonganKaryawan)
print("=====================================================")
print("Gaji Pokok    : Rp. ",gajiPokok)
print("Potongan({0}%): Rp. ({1}) ".format(potongan,PotonganGaji))
print("=====================================================")
print("Gaji Bersih   : Rp. ",(gajiPokok-PotonganGaji))
