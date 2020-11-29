from random import randint
print("Hai... nama saya Mr. Lappie, saya telah memilih bilangan bulat secara acak")
bil=randint(0,100)
point=100
while True:
    jawaban= int(input("Tebakan Anda= "))
    if(jawaban > bil):
        print("Hehehe... Bilangan tebakan anda terlalu besar")
        point-=2
    elif(jawaban < bil):
        print("Hehehe... Bilangan tebakan anda terlalu kecil")
        point-=2
    elif(jawaban == bil):
        print("Yeeee... Bilangan tebakan anda BENAR:)")
        break
print("Score anda= ", point)
