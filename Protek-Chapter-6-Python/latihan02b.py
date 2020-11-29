def starFormation1(n):
    for i in range (0, n):
        for j in range (0, i+1):
            print("* ", end= " ")
        print(" ")

starFormation1(4)

def starFormation2(n):
    for i in reversed (range (0, n)):
        for j in range (0, i+1):
            print("* ", end= " ")
        print(" ")

starFormation2(3)
    

