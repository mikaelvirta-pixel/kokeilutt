import random

n = int(input("Arpakuutioiden määrä: "))

summa = 0

for i in range(n):
    heitto = random.randint(1,6)
    summa += heitto

print("Silmälukujen summa on:", summa)


