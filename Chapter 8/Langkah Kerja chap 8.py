#list
print("1. List")
a=[1,5,6,3,6,9,11,20,12]
b=[7,4,5,6,7,1,12,5,9]
print(a)
print(b)

#sisipkan indeks
print("2. Sisipan indeks")
a.insert(2,10)
b.insert(1,15)
print(a)
print(b)

#sisipkan ke indeks terakhir
print("3. Sisipan ke indeks terakhir")
a.append(4)
b.append(8)
print(a)
print(b)

#sorting secara ascending
print("4. Sorting secara ascending")
a.sort()
b.sort()
print(a)
print(b)

#list yang elemennya adalah sublist dari list sebelumnya
print("5. List yang elemennya adalah sublist dari list sebelumnya")
c= a[0:8]
d= b[2:10]
print(c)
print(d)

#list yang elemennya adalah penjumlahan dari list sebelumnya
print("6. List yang elemennya adalah penjumlahan dari list sebelumnya")
e=[]
x=0
for x in range(len(c)):
    y=c[x]+d[x]
    e=e+[y]
print (e)

#list ke dalam Tuple
print("7. List ke dalam Tuple")
listE= tuple(e)
print(listE)

#nilai max, min, dan jumlah dari tuple
print("8. Nilai max, min, dan jumlah dari tuple")
nilaimax= max(listE)
nilaimin= min(listE)
hasil= sum(listE)
print("A. Nilai Maks= ", end= " ")
print(nilaimax)
print("B. Nilai Min= ", end= " ")
print(nilaimin)
print("C. Nilai Jumlah= ", end= " ")
print(hasil)

#variable yang berisi string
print("9. Variable yang berisi string")
myString = "python adalah bahasa pemrograman yang menyenangkan"
print(myString)

#karakter huruf apa saja yang terdapat pada string menggunakan set
karakter=set(myString)
print("10. Karakter hurufnya= ", end= " ")
print(karakter)

#string ke list lalu di urutkan 
listnya= list(karakter)
listnya.sort()
print("11' Karakter huruf setelah diurutkan= ", end= " ")
print(listnya)

