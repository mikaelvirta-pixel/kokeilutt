lista = []

lisaa = int(input("Lisää juttuja listaan ja lopeta nollalla lista: "))
while lisaa != 0:
    lista.append(lisaa)
    print(f"Lista nyt {lista}")
    lista.sort()
    print(f"Lista järjestyksessä {lista}")
    lisaa = int(input("Lisää juttuja listaan ja lopeta nollalla lista: "))
else:
    print("Heihei")
