kayttaja = input("Käyttäjän nimi")
if kayttaja == "Matti":
         print("Seuraava kiitos")
         quit()

annos =   float(input("Montako keittoannosta?: "))
hinta = annos * 5.90
print(f"Kokonaishinta on: {hinta} euroa")
print("Seuravava, kiitos")
