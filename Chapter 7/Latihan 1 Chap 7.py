a= input("Masukkan nama file (d:/anyfiles.txt): ")

file = open(a, "r")
print("Isi file ", a ,"adalah")
print(file.read())
