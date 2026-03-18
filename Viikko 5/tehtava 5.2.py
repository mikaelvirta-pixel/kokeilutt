luvut = []

while True:
    syota = input("Lisää joku luku: Tyhjä merkkijono lopettaa ohjelman")
    if syota == "":
        break

    luku = int(syota)
    luvut.append(luku)

    luvut.sort(reverse=True)

    viisi_suurinta = luvut[:5]

print("Viisi suurinta:", viisi_suurinta)