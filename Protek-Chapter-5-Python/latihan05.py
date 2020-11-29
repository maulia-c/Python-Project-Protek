kodeKaryawan= int(input("Masukkan kode Karyawan : "))
namaKaryawan= str(input("Masukkan Nama Karyawan : "))
golonganKaryawan= str(input("Masukkan Golongan  : "))

 #Golongan   
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

status= int(input("Masukkan Angka 1) Apabila Sudah Menikah 2) Apabila Belum Menikah: "))

if(status==1):
    statusnya="Sudah Menikah"
    jumlahAnak= int(input("Masukkan Jumlah Anak: "))
else:
    statusnya= "Belum Manikah"
    

#Tunjangan
if(status==1):
    TunjanganAnak= gajiPokok*jumlahAnak*(5/100)
    TunjanganIstri= gajiPokok*(10/100)
    
#GajiKotor
if(status==1):
    gajiKotor= gajiPokok+TunjanganIstri+TunjanganAnak
else:
    gajiKotor=gajiPokok

#HitungPotonganGaji
PotonganGaji= gajiPokok*(potongan/100)

#GajiBersih
gajiBersih= gajiKotor-PotonganGaji

    
#TampilanHasilGaji
print("================Struk Gaji Karyawan==================")
print("Nama Karyawan; ",namaKaryawan)
print("Kode Karyawan: ",kodeKaryawan)
print("Golongan:  ",golonganKaryawan)
print("Status: ",statusnya)
if(status==1):
    print("Jumlah Anak: ",jumlahAnak
          )
print("=====================================================")
print("Gaji Pokok    : Rp. ",gajiPokok)
if(status==1):
    print("Tunjangan Istri: Rp. ",TunjanganIstri)
    print("Tunjangan Anak: Rp.",TunjanganAnak)
print("=====================================================")
print("Gaji Kotor: Rp. ",gajiKotor)
print("Potongan({0}%): Rp. ({1}) ".format(potongan,PotonganGaji))
print("=====================================================")
print("Gaji Bersih   : Rp. ",(gajiKotor-PotonganGaji))

