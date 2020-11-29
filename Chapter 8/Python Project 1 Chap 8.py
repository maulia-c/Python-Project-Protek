jumlah= int(input("Masukkan jumlah bilangan= "))
listA= []

a=0
for a in range (0,jumlah):
    a+=1
    try:
        bil= int(input("Masukkan bilangan ke-"+ str(a) + " = "))
        listA.append(bil)
    except ValueError:
        print("Yang Anda Masukkan Bukan Bilangan")

listA.sort(reversed=True)
print("Urutan dari yang terbesar: ", listA)
