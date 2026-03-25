import math

def pizzan_hinta(halkaisija_cm, hinta):
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala = math.pi * sade_m * sade_m
    return hinta / pinta_ala


d1 = float(input("Anna pizzan 1 halkaisija (cm): "))
h1 = float(input("Anna pizzan 1 hinta (€): "))

d2 = float(input("Anna pizzan 2 halkaisija (cm): "))
h2 = float(input("Anna pizzan 2 hinta (€): "))

yks1 = pizzan_hinta(d1, h1)
yks2 = pizzan_hinta(d2, h2)

print("Pizza 1 yksikköhinta:", yks1)
print("Pizza 2 yksikköhinta:", yks2)

if yks1 < yks2:
    print("Pizza 1 on parempi valinta")
else:
    print("Pizza 2 on parempi valinta")