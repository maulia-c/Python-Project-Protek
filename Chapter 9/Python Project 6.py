nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
{'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
{'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
{'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
{'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("="*70)
print("NIM".ljust(10), "NAMA".ljust(15), "N. MID".rjust(5), "N. UAS".rjust(10), "N. Akhir".rjust(10), "STATUS".rjust(10))
print("="*70)
m = 0
for a in nilai:
    print(nilai[m]["nim"].ljust(10),end="")
    x = (nilai[m]["nama"].ljust(15))
    print(x,end="")
    y = str(nilai[m]["mid"]).rjust(5)
    print(y,end="")
    y= str(nilai[m]["uas"]).rjust(10)
    print(y.rjust(14),end="")
    nilaiAkhir= int((a["mid"] + 2 * a["uas"])/3)
    rumus=(nilaiAkhir)
    try:
        if (rumus >= 60):
            status = "LULUS"
        elif (rumus < 60):
            status = "TIDAK LULUS"
    except ValueError:
        print("salah")
    print(str(nilaiAkhir).rjust(10), status.rjust(11))
    m = m + 1
print("="*70)

