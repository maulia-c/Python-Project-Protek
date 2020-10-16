import math
TarifSewa= 200000
TarifTambahan= 10000

JamAwal= 6
JamAkhir= 23
MenitAwal= (0/60)
MenitAkhir= (50/60)

print ("LamaSewa")
LamaSewa=(math.floor(JamAkhir-JamAwal+MenitAkhir-MenitAwal))
print (LamaSewa)

Waktu1= 12
Waktu2= (LamaSewa-Waktu1)

BiayaSewa1= 200000
BiayaSewa2= (Waktu2*10000)

print ("TotalBiaya")
TotalBiaya= (BiayaSewa1+BiayaSewa2)
print (TotalBiaya)
