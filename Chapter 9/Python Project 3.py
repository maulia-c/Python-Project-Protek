import math
def bintang(n):
    if n > 0:
        if (n%2 !=0):
            n = math.ceil(n/2)
            for x in range(n):
                y = "*" + "**"*x
                print(y.center(40," "))
            a = 0
            rumus = n-1
            for x in range (rumus):
                a= a+1
                bintang= "*" + "**"*(rumus-a)
                print(bintang.center(40, " "))
        else:
            print("Angka yang kamu masukkan genap atau negatif \nUlangi lagi")

try:
    n= int(input("Masukkan jumlah n: "))
    if n <= 0:
        print("Ini bukan bilangan asli")
except NameError:
    print("n bukan bilangan")
except ValueError:
    print("n bukan bilangan")
    
bintang(n)
