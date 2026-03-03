muunnos = (float(input("Syötä numero muuttaksesi sen tuumista senttimetreiksi: ")))
while muunnos >= 0:
    sentit = muunnos * 2.54
    print(f" {muunnos} tuumaa on: {sentit}  senttimetriä")
    muunnos = float(input("Syötä tuumat, negatiivinen lopettaa"))


