def dataStat(x):
    data = len(x)
    jumlah = sum(x)
    rata = jumlah/data
    tertinggi = max(x)
    terendah = min(x)
    return [rata, tertinggi, terendah]

bil= [5,45,6,78,34,2,12]
print(dataStat(bil))
