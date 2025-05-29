file = open("piosenka.txt")
# for line in file:
#     print(line)
file.read()
# file.readline()
# print(file.readlines())
file.close()


def oblicz_sume_wydatkow(plik):
    file = open(plik)
    suma = 0
    for line in file:
        kwota = int(line)
        suma += kwota
    file.close()

# oblicz_sume_wydatkow("piosenka.txt")


# with open("piosenka.txt") as file:
#     for line in file:
#         print(line)
#


# class NaszAsystent:
#     def __enter__(self):
#         print("Prosimy żonę o pozowolenie")
#         print("Obiecujemy, że nie wrócimy za późno")
#
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Prosimy żonę o wybaczenie")
#         print("Kupujemy jej kwiaty")
#         print("Obiecujemy, że to ostatni raz")
#
#
# with NaszAsystent() as asystent:
#     print("Idziemy na piwo")
#     print("Pijemy piwo")
#     print("Wracamy do domu")
#

# with open("piosenka.txt", "w") as plik:
#     nowy_tekst = "Dodatkowa linijka\n"
#     plik.write(nowy_tekst)

# with open("piosenka.txt", "a") as plik:
#     nowy_tekst = "Dodatkowa linijka\n"
#     plik.write(nowy_tekst)
#
# with open("piosenka.txt", "w+") as plik:
#     for linia in plik:
#         print(linia)
#     nowy_tekst = "Dodatkowa linijka\n"
#     plik.write(nowy_tekst)

with open("piosenka2.txt", "r+") as plik:
    nowy_tekst = "\nDodatkowa linijka\n"
    plik.write(nowy_tekst)

# with open("piosenka1.txt", "a+") as plik:
#     nowy_tekst = "\nDodatkowa linijka\n"
#     plik.write(nowy_tekst)
#     for linia in plik:
#         print(linia)

