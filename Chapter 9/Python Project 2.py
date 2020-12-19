def bintang(n):
    for x in range(n):
        y = "*" + "**"*x
        print(y.center(40," "))

try:
    n= int(input("Masukkan jumlah n: "))
    if n <= 0:
        print("Ini bukan bilangan asli")
except NameError:
    print("n bukan bilangan bulat")
except ValueError:
    print("n bukan bilangan bulat")
    
bintang(n)

