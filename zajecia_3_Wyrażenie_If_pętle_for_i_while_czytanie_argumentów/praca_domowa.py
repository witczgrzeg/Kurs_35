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
print("Witam w naszym systemie paczek!")

liczba_paczek_razem = 1
numer_najlżejszej_paczki = 1
waga_calkowita = 0
suma_pustych_KG = 0
najlzejsza_paczka = 20
waga_paczki = 0


liczba_produktow = int(input("Podaj liczbę produktów: \n"))


for produkt in range(liczba_produktow):
    waga_elementu = int(input(f"Podaj wagę elementu #{produkt + 1}: \n"))

    if waga_elementu <1 or waga_elementu >10:
        print("Koniec dodawania paczek.")
        break
    waga_calkowita += waga_elementu

    if waga_elementu + waga_paczki > 20:
        if waga_paczki < najlzejsza_paczka:
            najlzejsza_paczka = waga_paczki
            numer_najlżejszej_paczki = liczba_paczek_razem

        liczba_paczek_razem += 1
        waga_paczki = waga_elementu
    else:
        waga_paczki += waga_elementu
if waga_paczki > 0:

    if waga_paczki < najlzejsza_paczka:
        najlzejsza_paczka = waga_paczki
        numer_najlżejszej_paczki = liczba_paczek_razem

liczba_pustych_kg = 20 * liczba_paczek_razem - waga_calkowita

print("Podsumowanie:")
#ilość wysłanych paczek
print(f"Wysłano {liczba_paczek_razem} paczek.")
#łączna waga wszystkich paczek
print(f"Wysłano {waga_calkowita} KG.")
#suma pozostałych KG w paczce, żeby nie przekraczać 20KG
print(f"Suma pustych kilogramów: {liczba_pustych_kg}")
#trzeba podać która paczka waży najmniej
print(f"Najwięcej pustych kilogramów ma paczka: {numer_najlżejszej_paczki}")
