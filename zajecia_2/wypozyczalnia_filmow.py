"""
Wypożyczalnia filmów

Wczytaj od użytkownika:
- wiek (liczba całkowita),
- czy ma zgodę rodzica (tak/nie).

Oblicz:
- ma_dostep_18plus (wiek >= 18),
- ma_dostep_13plus (wiek >= 13 lub zgoda == "tak").

Wyświetl:
- "Filmy 18+", "Filmy 13+" albo "Tylko bajki" zależnie od wieku i zgody, bez ifów.
"""

wiek = int(input("Podaj swoj wiek:"))
zgoda = input("Czy masz zgode rodzica? (tak/nie): ")
zgoda = zgoda.lower()

zgoda_potwierdzona = zgoda == "tak"
ma_dostep_18plus = wiek >= 18
ma_dostep_13plus = wiek >= 13 or zgoda_potwierdzona

# print(f"Uzytkownik ma {wiek} lat.")
# print(f"Uzytkownik ma zgode rodzica: {zgoda_potwierdzona}")
# print(f"Uzytkownik ma dostep do filmow 18+: {ma_dostep_18plus}")
# print(f"Uzytkownik ma dostep do filmow 13+: {ma_dostep_13plus}")
print("Filmy 18+" * ma_dostep_18plus + "Filmy 13+" * ma_dostep_13plus + "Tylko bajki" * (not ma_dostep_18plus and not ma_dostep_13plus))

print(0 == False)