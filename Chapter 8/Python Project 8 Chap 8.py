def rataharga (a):
    harga = list(a.values())
    jumlah = sum(harga)
    banyak = 0
    for b in harga:
        banyak+=1
    rerata = jumlah/banyak
    return rerata

a={'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' :6500}
print(rataharga(a))
