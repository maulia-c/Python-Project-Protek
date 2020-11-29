#Penambahan except
try:
    file = open("c:/myfile.txt", "r")
    print(file.read)
except FileNotFoundError:
    print("File tidak ditemukan")
