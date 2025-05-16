from collections.abc import Iterable
#
# lista_uczniow = ["Jan", "Anna", "Piotr", "Kasia", "Tomek"]
# print(isinstance(lista_uczniow, Iterable))
# # for uczen in lista_uczniow:
# #     print(uczen)
#
print(isinstance(range(20), Iterable))
print(isinstance("Michal", Iterable))
#
# for number in range(20):
#     print(number)
#
#
# ilosc_paczek = int(input("Podaj ilość paczek: "))
# waga_wszystkich_paczek = 0
# for paczka in range(ilosc_paczek):
#     print(paczka)
#     waga_paczki = float(input("Podaj wagę paczki: "))
#     waga_wszystkich_paczek += waga_paczki
#
# print(f"Waga wszystkich paczek wynosi: {waga_wszystkich_paczek} kg")


for char in "Michal":
    print(char)

######################################
"""
for <tymczasowa_zmienna> in <iterowalny_obiekt>:
    <blok_kodu>

"""