print ("Diagram Jumlah Mahasiswa Laki-Laki dan Perempuan")

MahasiswaLaki= int(input("Masukkan Jumlah Mahasiswa Laki-Laki=> "))
MahasiswaPerempuan= int(input("Masukkan Jumlah Mahasiswa Perempuan=> "))

outputLaki= int(MahasiswaLaki//10)
outputPerempuan= int (MahasiswaPerempuan//10)

print ("Laki-Laki = ", outputLaki*"*", MahasiswaLaki)
print ("Perempuan = ", outputPerempuan*"*", MahasiswaPerempuan)

