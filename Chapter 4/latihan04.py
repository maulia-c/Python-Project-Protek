import math
JarakAB= 125
KecepatanAB=62
JarakBC=256
KecepatanBC=70

#Waktu Dalam Menit
WaktuAB= math.ceil(JarakAB/KecepatanAB*60)
WaktuBC= math.ceil(JarakBC/KecepatanBC*60)
Istirahat= 45

JumlahWaktu= (WaktuAB+WaktuBC+Istirahat)

WaktuAwal=6
JumlahWaktuDalamJam= (JumlahWaktu//60)+WaktuAwal
JumlahWaktuDalamMenit= (JumlahWaktu%60)

print ("Pak Amir sampai di kota C pukul", (JumlahWaktuDalamJam)," ",(JumlahWaktuDalamMenit))

