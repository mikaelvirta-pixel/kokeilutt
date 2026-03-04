tuntipalkka = float(input("Tuntipalkkasi? : "))
tunnit = float(input("Tehdyt tunnit? : "))
paiva = input("Mikä viikonpäivä? : ")
palkka = tunnit * tuntipalkka
sunnuntaipalkka = tunnit * tuntipalkka * 2
if paiva == "Sunnuntai":
    print(f"Päiväpalkkasi on:  {sunnuntaipalkka} euroa")
    quit()

print(f"Päiväpalkkasi on: {palkka} euroa")