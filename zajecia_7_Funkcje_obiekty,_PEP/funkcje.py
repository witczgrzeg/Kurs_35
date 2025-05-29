# miasta = [('Warszawa', 25), ('Kraków', 20), ('Wrocław', 15), ('Gdańsk', 10), ('Poznań', 5)]
# for miasto, temperatura in miasta:
#     temp_f = temperatura * 9/5 + 32
#     print(f'Temperatura w {miasto} wynosi {temperatura}°C, co odpowiada {temp_f}°F')


# x = 10/3
# print(round(x, 2))

# def obliczanie_temperatury_w_fahrenheit_dla_miasta(krotka_z_miastem):
#     nazwa_miasta, temperatura_w_celsjuszach = krotka_z_miastem
#     print(f"Obliczanie temperatury w Fahrenheit dla miasta: {nazwa_miasta}")
#     temperatura_fahrenheit = temperatura_w_celsjuszach * 9/5 + 32
#     print(f"Temperatura w {nazwa_miasta} wynosi {temperatura_w_celsjuszach}°C, co odpowiada {temperatura_fahrenheit}°F")
#
# # obliczanie_temperatury_w_fahrenheit_dla_miasta("Szczecin", 15)
# # obliczanie_temperatury_w_fahrenheit_dla_miasta("Warszawa", 25)
# obliczanie_temperatury_w_fahrenheit_dla_miasta(("Kraków", 20))
# obliczanie_temperatury_w_fahrenheit_dla_miasta(("Sztokholm", 10))
#
# def przywitaj_sie():
#     print("Hello world!")
#
# przywitaj_sie()
#
# def obliczanie_temperatury_w_fahrenheit_dla_miasta(nazwa_miasta, temperatura_w_celsjuszach):
#     print(f"Obliczanie temperatury w Fahrenheit dla miasta: {nazwa_miasta}")
#     temperatura_fahrenheit = temperatura_w_celsjuszach * 9/5 + 32
#     print(f"Temperatura w {nazwa_miasta} wynosi {temperatura_w_celsjuszach}°C, co odpowiada {temperatura_fahrenheit}°F")
#
# obliczanie_temperatury_w_fahrenheit_dla_miasta(nazwa_miasta="Szczecin", temperatura_w_celsjuszach=40)
# obliczanie_temperatury_w_fahrenheit_dla_miasta("Warszawa", 25)
# obliczanie_temperatury_w_fahrenheit_dla_miasta("Kraków", temperatura_w_celsjuszach=14)
# obliczanie_temperatury_w_fahrenheit_dla_miasta(temperatura_w_celsjuszach=40, nazwa_miasta="Poznań")
#
#
#
# def sprawdz_czy_uzytkownik_jest_dorosly(wiek):
#     if wiek >= 18:
#         print("Użytkownik jest pełnoletni.")
#         print("Możesz kupić alkohol, papierosy i napój energetyczny.")
#     else:
#         print("Użytkownik jest niepełnoletni.")
#         print("Nie możesz kupić alkoholu, papierosów ani napoju energetycznego.")
#
# print("Witaj w naszej żabce!")
#
# cena_zakupow = 0
#
# while True:
#     nazwa_produktu = input("Podaj nazwę produktu: ")
#     if nazwa_produktu == "":
#         break
#     cena_produkt = float(input("Podaj cenę produktu: "))
#     if nazwa_produktu in ("alkohol", "papierosy", "napój energetyczny"):
#         wiek = int(input("Podaj swój wiek: "))
#         pelnoletni = sprawdz_czy_uzytkownik_jest_dorosly(wiek)
#         if not pelnoletni:
#             print("Nie możesz kupić tego produktu.")
#             continue
#     cena_zakupow += cena_produkt
#
# print(cena_zakupow)
#
#
#
# def dodawanie(x, y):
#     wynik = x + y
#     print(wynik)
#     return wynik
#
# wynik_dodawania = dodawanie(2, 3)
# print(wynik_dodawania)


def sprawdzenie_emerytury(wiek, pensja, pozycja):
    wiek_do_emerytury = 65 - wiek
    if wiek_do_emerytury < 0:
        print("Jesteś na emeryturze")
        return pensja
    print("Obliczamy emeryturę")
    if pozycja == "programista":
        emerytura = pensja * 0.01
    elif pozycja == "nauczyciel":
        emerytura = pensja * 0.80
    else:
        emerytura = pensja * 0.50
    print("Obliczylismy emeryturę dla osoby pracującej")
    return emerytura


emerytura = sprawdzenie_emerytury(wiek=67, pensja=5000, pozycja="programista")
print(emerytura)
