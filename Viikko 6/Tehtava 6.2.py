import random

def noppa(tahkot):
    return random.randint(1, tahkot)

tahkot = int(input("Anna nopan tahkojen määrä:  "))

print("Heitetään noppaa")
silmaluku = 0

while silmaluku != tahkot:
    silmaluku = noppa(tahkot)
    print(silmaluku)