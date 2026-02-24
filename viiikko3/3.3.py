sukupuoli = input("Sukupuolesi? (Mies/Nainen): ")
hemoglobiini = int(input(   "Hemoglogiiniarvosi? g/l: "))

if sukupuoli == "Mies":
    if hemoglobiini < 134:
        print("Hemoglobiini alhainen")
    elif hemoglobiini <= 195:
        print("Hemoglobiini on normaali.")
    else:
        print("Hemoglobiini on korkea.")

elif sukupuoli == "Nainen":
    if hemoglobiini < 117:
        print("Hemoglobiini alhainen")
    elif hemoglobiini <= 175:
        print("Hemoglobiini on normaali.")
    else:
        print("Hemoglobiini on korkea.")