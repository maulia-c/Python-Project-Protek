def harga(buah):
    rp = list(buah.values())
    rp.sort(reverse=True)
    termahal = rp[0]
    for a, rp in buah.items():
        if rp == termahal:
            return a
a = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print(harga(a))

