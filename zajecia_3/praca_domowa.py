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

liczba_produktow = int(input("Podaj liczba produktów: \n")) #wpisuje liczbę paczek

# paczka = []
# paczki = []
# waga_produktu = 0 #waga jednej paczki
# liczba_paczek_wyslanych = [] # suma paczek podanych
# liczba_kg_wyslanych = 0 # suma wagi paczek5
# suma_pustych_kg = 0 # suma ile kg pozostało do 20kg w jednej paczce + suma wszystkich paczek
#
# for ilosc in range(liczba_produktow):
#     waga_produktu = int(input(f"Podaj wagę produktu {ilosc +1}: \n")) #podaje wagę do każdej paczki wpisanej w paczka
#
#     if waga_produktu  <1 or waga_produktu >10:
#         print("Nie poprawna waga produktu! Waga produktu nie może przekraczać 10 GK") #informuje że produkt jezt za ciężki
#         if paczka:
#             ilosc.append(paczki)
#         break
#     if waga_produktu + liczba_kg_wyslanych > 20:
#         paczka.append(paczki)
#     else:
#             liczba_kg_wyslanych += waga_produktu
# print (f"{liczba_kg_wyslanych},{paczka}")

paczki = []
paczka = []
waga_paczki = 0
waga_całkowita = 0

for p in range(liczba_produktow):
    waga_prod = int(input(f"Podaj wagę produktu {p+1}: \n"))

if liczba_produktow:
    waga_prod.append(waga_paczki)
print()