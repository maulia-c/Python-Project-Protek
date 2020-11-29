nama = ["jambu", "rambutan", "durian", "apel"]
print("Data= ", nama)

def sortStringByChar(nama):
    nama.sort(key = len, reverse = True)
    print("Data berdasarkan banyak karakter= ",nama)
sortStringByChar(nama)
    
