def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial (n - 1)

def combine(x, y):
    hasil = faktorial(x)//(faktorial(y)*faktorial(x-y))
    print ("C(5,3)= ",hasil)

def permutation(x,y):
    hasil = faktorial(x)//faktorial(x-y)
    print ("P(10,7)= ",hasil)


#Combination
x,y= 5,3
combine(5, 3)

#Permutation
x,y= 10,7
permutation(10, 7)


