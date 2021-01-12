def diffDate(x):
    import datetime
    skrg = datetime.datetime.now()
    from datetime import datetime
    awal = datetime.strptime(x, "%Y-%m-%d")
    rms = awal - skrg
    print(abs(rms.days))

diffDate("2019-12-24")
