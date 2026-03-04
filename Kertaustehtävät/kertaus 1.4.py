sanat = []

while True:
    sana = input("Anna sana lisättäväksi tarinaan, lopeta tarina kirjoittamalla loppu: ")

    if sana == "loppu":
        print(" ".join(sanat))
        break

    else:
        sanat.append(sana)

