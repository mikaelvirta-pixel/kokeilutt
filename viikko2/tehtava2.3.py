kanta_string = input(f"Kirjoita tähän suorakulmion kanta: ")

kanta = float(kanta_string)

korkeus_string = input(f"Ja sitten korkeus: ")

korkeus = float(korkeus_string)

pintaala = kanta * korkeus

piiri = kanta * korkeus *2

print("Suorakulmion pinta-ala on: " + str(pintaala) + " neliötä" + " ja piiri on " + str(piiri) + " metriä")

