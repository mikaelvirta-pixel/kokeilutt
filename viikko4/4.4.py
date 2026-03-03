import random
value = random.randint(1, 10)


while True:
    arvaus = int(input("Arvaa numero välillä 1-10! :"))

    if arvaus == value:
        print("Oikein")
        break

    if arvaus < value:
        print("Liian pieni arvaus")
    if arvaus > value:
         print("Liian suuri arvaus")

