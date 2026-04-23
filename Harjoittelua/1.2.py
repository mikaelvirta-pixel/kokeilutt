oppilaita = {
   "Karoliina": ["Karoliina", 2022, "Historia"],
    "Eveliina": ["Eveliina", 2020, "Liikunta"],
   "Jesse": ["Jesse", 2021, "Matematiikka"],
    "Kerkko": ["Kerkko", 2021, "Ruokailu"]
}

print(oppilaita["Karoliina"], 2)
print(oppilaita["Jesse"], 3)

oppilaita["Kari"] = ["Kari", 2025, "Filosofia"]

del oppilaita["Eveliina"]
print (oppilaita)