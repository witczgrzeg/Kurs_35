# uzytkownik = ["Michał", "Ziętkowski", 20, True]

uzytkownik = {
    "imie": "Michał",
    "nazwisko": "Ziętkowski",
    "wiek": 20,
    "czy_uczen": True,
}
# print(uzytkownik)
#
# print(uzytkownik["imie"])
# #print(uzytkownik["plec"])
# print(uzytkownik.get("plec"))
#
#
# ###### dodawanie nowych wartosci
# uzytkownik["plec"] = "mezczyzna"
#
# print(uzytkownik)
#
# uzytkownik["plec"] = "kobieta"
# print(uzytkownik)
#
# print(uzytkownik)
# ######## usuwanie par klucz wartosc ze slownika
# del uzytkownik["plec"]
#
# print(uzytkownik)
#
# uzytkownik.pop("imie")
# print(uzytkownik)

############# iteracji

for item in uzytkownik:
    print(item)

# for value in uzytkownik.values():
#     print(value)

for key in uzytkownik.keys():
    print(key)

for key, value in uzytkownik.items():
    print(f"{key}: {value}")

if "adres" in uzytkownik:
    del uzytkownik["adres"]
else:
    print("Nie ma takiego klucza")
# del uzytkownik["adres"]

################### zly przyklad na iteracje po liscie
# lista_rzeczy = [1, 2, 3, 4, 5]
#
#
# for key, value in lista_rzeczy:
#     print(f"{key}: {value}")