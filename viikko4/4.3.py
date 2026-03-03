lukuja = []

while True:
    syote = input("Anna numero (tyhjä lopettaa): ")

    if syote == "":
        break

    try:
        luku = float(syote)
        lukuja.append(luku)
    except ValueError:
        print("Syötäthän vain numeroita.")

if lukuja:
    print("Pienin luku:", min(lukuja))
    print("Suurin luku:", max(lukuja))
else:
    print("Et laittanut mitään lukua.")