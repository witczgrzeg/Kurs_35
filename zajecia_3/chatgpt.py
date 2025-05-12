print("Witam w naszym systemie paczek!")

liczba_produktow = int(input("Podaj liczbę produktów: \n"))

pelna_paczka = []
suma_paczek = []
waga_paczki = 0

for p in range(liczba_produktow):
    waga_prod = int(input(f"Podaj wagę produktu {p + 1}: \n"))

    if waga_prod < 1 or waga_prod > 10:
        print("Produkt przekracza limit wagowy (1–10 kg). Przerywam dodawanie paczek.")
        break

    if waga_paczki + waga_prod > 20:
        suma_paczek.append(pelna_paczka)
        pelna_paczka = [waga_prod]
        waga_paczki = waga_prod
    else:
        pelna_paczka.append(waga_prod)
        waga_paczki += waga_prod

# dodanie ostatniej paczki, jeśli coś zawiera
if pelna_paczka:
    suma_paczek.append(pelna_paczka)

# Podsumowanie
print("\n=== PODSUMOWANIE ===")
print(f"Wysłano {len(suma_paczek)} paczek")

# Suma wysłanych kg
suma_kg = sum(sum(paczka) for paczka in suma_paczek)
print(f"Wysłano {suma_kg} kg")

# Suma pustych kg
puste_kg = len(suma_paczek) * 20 - suma_kg
print(f"Suma pustych kilogramów: {puste_kg} kg")

# Paczka z największą liczbą pustych kg
najwiecej_pustych = 0
nr_paczki = 0

for i, paczka in enumerate(suma_paczek, start=1):
    puste = 20 - sum(paczka)
    if puste > najwiecej_pustych:
        najwiecej_pustych = puste
        nr_paczki = i

print(f"Najwięcej pustych kilogramów ma paczka {nr_paczki} ({najwiecej_pustych} kg)")