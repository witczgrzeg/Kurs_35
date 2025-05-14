"""
Pętle i argumenty w konsoli

Napisz program do obsługi ładowarki paczek. Po uruchomieniu, aplikacja pyta ile paczek chcesz wysłać, a następnie wymaga podania wagi dla każdej z nich.

Na koniec działania program powinien wyświetlić w podsumowaniu:

Liczbę paczek wysłanych
Liczbę kilogramów wysłanych
Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych
Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik

Restrykcje:

Waga elementów musi być z przedziału od 1 do 10 kg.
Każda paczka może maksymalnie zmieścić 20 kilogramów towaru.
W przypadku, jeżeli dodawany element przekroczy wagę towaru, ma zostać dodany do nowej paczki, a obecna wysłana.
W przypadku podania wagi elementu mniejszej od 1kg lub większej od 10kg, dodawanie paczek zostaje zakończone i wszystkie paczki są wysłane. Wyświetlane jest podsumowanie.

Przykład 1:

Ilość elementów: 2
Wagi elementów: 7, 9
Podsumowanie:

Wysłano 1 paczkę (7+9)
Wysłano 16 kg
Suma pustych kilogramów: 4kg
Najwięcej pustych kilogramów ma paczka 1 (4kg)

Przykład 2:

 Ilość elementów: 6
Wagi elementów: 3, 6, 5, 8, 2, 3
Podsumowanie:

Wysłano 2 paczki (3+6+5, 8+2+3)
Wysłano 27 kg
Suma pustych kilogramów: 13kg
Najwięcej pustych kilogramów ma paczka 2 (7kg)

Przykład 3:
 Ilość elementów: 8

Wagi elementów: 7, 14
 Podsumowanie:
Wysłano 1 paczkę (7)
Wysłano 7 kg
Suma pustych kilogramów: 13kg
Najwięcej pustych kilogramów ma paczka 13

"""
# print("Witam w naszym systemie paczek!")
#
# liczba_produktow = int(input("Podaj liczba produktów: \n")) #wpisuje liczbę paczek
#
# pelna_paczka = []
# suma_paczek = []
# waga_paczki = 0
#
# for p in range(liczba_produktow):
#     waga_prod= int(input(f"Podaj wagę paczki {p + 1} \n"))
#
#     if waga_prod < 1 or waga_prod > 10:
#         print("Produkt przekracza limit wagowy (1–10 kg). Przerywam dodawanie paczek.")
#         break
#     if waga_paczki + waga_prod > 20:
#
# if pelna_paczka:
#
#
# print(suma_paczek)
# print(pelna_paczka)


# print("Witamy w naszym systemie paczek!")
# ilosc_elementow = int(input("Podaj ilość paczek: \n"))
#
# suma_paczek = 0
#
# for paczka in range(ilosc_elementow):
#     waga_paczki= int(input(f"Podaj wagę paczki {paczka+1}: \n"))
#     if waga_paczki <=1 or waga_paczki >=10:
#         print("Końćzę dodawanie paczki. Paczka wysłana.")
#         break
#     if waga_paczki >20:
#         suma_paczek += waga_paczki
#         waga_paczki = suma_paczek
# print(suma_paczek)

# print("Witam w naszym systemie paczek!")
# liczba_produktow = int(input("Podaj liczbę produktów: \n"))
#
# suma_wag = 0
# liczba_paczek = 0
#
# for paczka in range(liczba_produktow):
#     waga_paczki = int(input(f"Podaj wagę paczki #{paczka+1}: \n"))
#
#
#     if waga_paczki <1 or waga_paczki >10:
#         print("Koniec dodawania paczek.")
#         break
#     suma_wag += waga_paczki
#
#     if suma_wag >=20:
#         waga_paczki = suma_wag
#         liczba_paczek += paczka
#
#
#
# print("Suma wag paczek wynosi:", suma_wag)
# print("liczba paczek wynosi:", liczba_paczek)


print("Witam w naszym systemie paczek!")

while True:
    liczba_produktow = int(input("Podaj liczbę produktów: \n"))
    suma_wag = 0
    liczba_paczek = 0

    for paczka in range(liczba_produktow):
        waga_paczki = int(input(f"Podaj wagę paczki #{paczka+1}: \n"))

        if waga_paczki <1 or waga_paczki >10:
            print("Koniec dodawania paczek.")
        suma_wag += waga_paczki

        if suma_wag + waga_paczki >=20:
            waga_paczki = suma_wag
            liczba_paczek +=

        else:
            suma_wag += waga_paczki
    else:
        break

print("Suma wag paczek wynosi:", suma_wag)
print("liczba paczek wynosi:", liczba_paczek)