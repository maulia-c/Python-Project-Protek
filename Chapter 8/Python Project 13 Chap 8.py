nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Aku', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

def maxnilai(x):
    maks= 0
    data = {}
    for w in x:
        UAS = w.get("uas")
        MID= w.get("mid")
        hitung = (MID + 2*UAS)/3
        if(hitung>maks):
            maks = hitung
            data["nim"] = w.get("nim")
            data["nama"] = w.get("nama")
    print("Nilai tertinggi draih oleh mahasiswa bernama ", data["nama"] ,"dengan NIM", data["nim"])
#Pemanggilan def
maxnilai(nilaiMhs)
