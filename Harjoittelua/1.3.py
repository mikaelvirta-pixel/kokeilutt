kirjasto = {
    "Taru Sormusten Herrasta": ["JRR TOlkien", 1938, "Fantasia"],
    "Raamattu": ["Joku", 0, "Fantasia"],
    "Sadan vuoden yksinäisyys": ["Joku kolumbialainen", 1954, "Kaunokirjallisuus"]
}

kirjasto["Raamattu"][2] = "Kauhu"

kirjasto["Kauhua"] = ["Jari", 2025, "Kauhu"]
del kirjasto["Sadan vuoden yksinäisyys"]
print(kirjasto)