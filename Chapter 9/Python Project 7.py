mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print("="*70)
print("NIM".ljust(8),"NAMA MAHASISWA".ljust(23), "TGL LAHIR".ljust(25), "TEMPAT LAHIR")
print("-"*70)

for data in mhs:
    ganti = data.split(":")
    print(ganti[0].ljust(9),end="")
    nama = (ganti[1])
    print(ganti[1].ljust(24),end="")
    tempat = ganti[2]
    tgl = tempat.replace("-","/")
    print(tgl.ljust(26),end='')
    nama = (ganti[3])
    print(ganti[3].ljust(75))

print('-'*70)
