sanakirja = {
    "John": ["John", 30, "Engineer"],
    "Emily": ["Emily", 25, "Artist"],
    "Anna": ["Anna", 11, "Student"]
}
print(sanakirja)

print(sanakirja["John"][0])
print(sanakirja["John"][1])
print(sanakirja["Emily"][2])
sanakirja["Anna"][2] = "Teacher"
sanakirja["James"] = ["James", 28, "Writer"]

print(sanakirja)

sanakirja["Sophia"] = ["Sophia", 35, "Lääkäri"]
del sanakirja["Emily"]
print (sanakirja)