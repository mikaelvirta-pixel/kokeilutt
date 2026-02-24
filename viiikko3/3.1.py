pituus = int(input("Kuhan pituus? cm: "))
if pituus <37:
    puuttuu = 37 - pituus
    print(f"Kuha on alimittainen, kuha takaisin järveen siitä puuttuu {puuttuu} cm")
else:
    print ("Hieno Kuha!")
