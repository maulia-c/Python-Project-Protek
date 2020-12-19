def ubahHuruf (a,b,c):
    ke1 = a
    ke2 = b
    ke3 = c
    for x in range(len(ke3)):
        ke1 = ke1.replace(ke2[x],ke3[x])
    print(ke1)

ubahHuruf("MATEMATIKA", "T", "S")




    
