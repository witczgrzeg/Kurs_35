print("Paczkomat 3000 – program do ładowania paczek")

num_elements = int(input("Podaj liczbę elementów: "))

packages = []
current_package = []
current_weight = 0
total_weight = 0

for i in range(num_elements):
    weight = int(input(f"Podaj wagę elementu {i+1}: "))

    if weight < 1 or weight > 10:
        print("Nieprawidłowa waga. Kończę ładowanie paczek.")
        if current_package:
            packages.append(current_package)
        break

    if current_weight + weight > 20:
        packages.append(current_package)
        current_package = [weight]
        current_weight = weight
    else:
        current_package.append(weight)
        current_weight += weight

    total_weight += weight

# Dodaj ostatnią paczkę, jeśli nie została jeszcze dodana
if current_package:
    packages.append(current_package)

# Podsumowanie
print("\n--- Podsumowanie ---")
print(f"Wysłano {len(packages)} paczek.")
print(f"Wysłano {total_weight} kg.")

empty_kgs = len(packages) * 20 - total_weight
print(f"Suma pustych kilogramów: {empty_kgs} kg")

max_empty = 0
max_empty_index = 0

for i, package in enumerate(packages):
    empty = 20 - sum(package)
    if empty > max_empty:
        max_empty = empty
        max_empty_index = i + 1

print(f"Najwięcej pustych kilogramów ma paczka {max_empty_index} ({max_empty}kg)")
