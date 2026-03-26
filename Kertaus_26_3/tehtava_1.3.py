lista = ["Kerkkoo", "Jumalan siunausta", "Halleluja", "Python on mukavaa", "Eror", "jaa"]

print(("Katsotaan montako sanaa listassa on jossa yli 5 kirjainta jee"))
laskuri = 0
for sana in lista:
    if len(sana) >5:
        laskuri = laskuri + 1

print(laskuri)

