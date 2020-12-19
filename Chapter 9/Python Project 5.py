nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
{'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
{'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
{'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
{'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("="*60)
print("NIM".ljust(10), "NAMA".ljust(15), "N. MID".rjust(5), "N. UAS".rjust(10))
print("="*60)
m = 0
for a in nilai:
    print(nilai[m]["nim"],end="")
    x = len(nilai[m]["nama"])
    print(nilai[m]["nama"].rjust(5+x),end="")
    y = str(nilai[m]["mid"])
    print(y.rjust(21-x),end="")
    y= str(nilai[m]["uas"])
    print(y.rjust(16))
    m = m+1
print("="*60)
