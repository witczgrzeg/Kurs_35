zbior_kolory = {"czerwony", "zielony", "niebieski", 23, True, ("Adam", "Kowalski")}
print(zbior_kolory)
print(id(zbior_kolory))
zbior_kolory.add("żółty")
print(id(zbior_kolory))
# print(zbior_kolory[0])
zbior_kolory.add("czerwony")
print(zbior_kolory)

zbior_kolory.remove("czerwony")

print(zbior_kolory)
for element in zbior_kolory:
    print(element)

lista_kolorow = list(zbior_kolory)
print(lista_kolorow)