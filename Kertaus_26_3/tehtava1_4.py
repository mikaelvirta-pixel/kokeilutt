def kuusi(koko):
    print("Tämä on kuusi")
    for i in range(koko):
        print(" " * (koko - i - 1) + "*" * (2 * i +1))
    print(" " * (koko -1) + "*")

numero = int(input("Anna numero 1-9: "))
if 1 <= numero <= 9:
    kuusi(numero)
else:
    print("Anna numero väliltä 1-9")

