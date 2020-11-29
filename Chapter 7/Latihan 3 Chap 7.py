print("------------------------------")
print("PROGRAM HITUNG RATA_RATA")
print("------------------------------")

a=0
sum=0
while True:
    try:
        bil=int(input("Masukkan bilangan bulat= "))
        sum+=bil
        a+=1
        ulang= input("lagi(y/n)? ")
        if ulang== "n":
            rerata=sum/a
            print("Hasil rata-rata= ", rerata)
            break
    except ValueError:
        print("Bukan Bilangan Bulat")
            
        

        
        
