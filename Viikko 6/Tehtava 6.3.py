def gallonat(g):
    return g * 3.785

while True:
    g = float(input("Anna gallonat: "))

    if g < 0:
        break

    print(g, "gallonaa on", gallonat(g), "litraa")