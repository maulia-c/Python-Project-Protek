def sum(*all):
    m=0
    for x in all:
        m+=x
    print(m)

def average(*all):
    m=0
    n=0
    for x in all:
        m+=x
        n+=1
    avg=m/n
    print(avg)
        

def max (*all):
    m=all[0]
    for x in all:
        if(x>m):
           m=x
    print(m)

def min(*all):
    m=all[0]
    for x in all:
        if(x<m):
            m=x
    print(m)

