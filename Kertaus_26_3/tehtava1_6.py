def yhteen(a, b):
    return a + b

def vahennys(a, b):
    return a - b

def kertolasku(a, b):
    return a * b

def jakolasku(a, b):
    return a / b


print("TERVETULOA KÄYTTÄMÄÄN LASKINTA!")

while True:
    print("\nValitse mitä toimintoa haluat käyttää:\n A: Yhteenlasku \n B: Vähennyslasku \n C: Kertolasku"
          "\n D: Jakolasku")

    valinta = input("Valintasi (A-D, Q lopettaa): ")

    if valinta == "Q":
        print("Ohjelma lopetetaan.")
        break

    a = float(input("Anna eka luku: "))
    b = float(input("Anna toka luku: "))

    if valinta == "A":
        print("Lukujen summa on:", yhteen(a, b))
    elif valinta == "B":
        print("Lukujen erotus on:", vahennys(a, b))
    elif valinta == "C":
        print("Lukujen tulo on:", kertolasku(a, b))
    elif valinta == "D":
        print("Lukujen osamäärä on:", jakolasku(a, b))
    else:
        print("Virheellinen valinta tai luku.")