tarkistus = int(input("Syötä numero tarkistaaksesi onko se alkuluku: "))

if tarkistus < 2:
    print("Ei oo alkuluku")
else:
    on_alkuluku = True

    for i in range(2, tarkistus):
            if tarkistus % i == 0:
             on_alkuluku = False
             break

    if on_alkuluku:
        print("On alkuluku")
    else:
        print("Ei alkuluku")



