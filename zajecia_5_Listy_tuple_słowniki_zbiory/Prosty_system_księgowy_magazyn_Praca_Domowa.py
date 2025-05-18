"""
Napisz program, który będzie rejestrował operacje na koncie firmy i stan magazynu.

Program po uruchomieniu wyświetla informację o dostępnych komendach:

saldo
 sprzedaż
zakup
konto
lista
magazyn
przegląd
koniec

Po wprowadzeniu odpowiedniej komendy, aplikacja zachowuje się w unikalny sposób dla każdej z nich:

1. saldo - Program pobiera kwotę do dodania lub odjęcia z konta.
2. sprzedaż - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi znajdować się w magazynie. Obliczenia respektuje względem konta i magazynu (np. produkt "rower" o cenie 100 i jednej sztuce spowoduje odjęcie z magazynu produktu "rower" oraz dodanie do konta kwoty 100).
3. zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do komendy "sprzedaz". Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
4. konto - Program wyświetla stan konta.
5. lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
6. magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
7. przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane pod indeksami od „od” do „do”. Jeżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać przegląd od początku lub/i do końca. Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).
8. koniec - Aplikacja kończy działanie.

Dodatkowe wymagania:

1. Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec".
2. Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc użyć komendy "przeglad".
3. Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację o dostępnych komendach, a także prosi o wprowadzenie jednej z nich.
4. Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji (np. przy komendzie "zakup" jeśli dla produktu podamy ujemną kwotę, aplikacja powinna wyświetlić informację o niemożności wykonania operacji i jej nie wykonać). Zadbaj też o prawidłowe typy danych.

"""


produkty_startowe = [
    {"nazwa": "mleko", "cena": 5, "ilosc": 20},
    {"nazwa": "jajka", "cena": 10, "ilosc": 30},
    {"nazwa": "chleb", "cena": 4, "ilosc": 15},
    {"nazwa": "masło", "cena": 8, "ilosc": 10},
    {"nazwa": "ser żółty", "cena": 12, "ilosc": 12},
    {"nazwa": "woda mineralna", "cena": 3, "ilosc": 25},
    {"nazwa": "cola", "cena": 6, "ilosc": 18},
    {"nazwa": "sok pomarańczowy", "cena": 7, "ilosc": 20},
    {"nazwa": "ryż", "cena": 9, "ilosc": 16},
    {"nazwa": "makaron", "cena": 6, "ilosc": 22},
    {"nazwa": "kawa", "cena": 20, "ilosc": 14},
    {"nazwa": "herbata", "cena": 15, "ilosc": 17},
    {"nazwa": "cukier", "cena": 5, "ilosc": 25},
    {"nazwa": "mąka", "cena": 4, "ilosc": 19},
    {"nazwa": "olej", "cena": 10, "ilosc": 13},
    {"nazwa": "ketchup", "cena": 7, "ilosc": 11},
    {"nazwa": "musztarda", "cena": 6, "ilosc": 10},
    {"nazwa": "majonez", "cena": 9, "ilosc": 8},
    {"nazwa": "płatki śniadaniowe", "cena": 11, "ilosc": 12},
    {"nazwa": "czekolada", "cena": 5, "ilosc": 30},
    {"nazwa": "baton", "cena": 3, "ilosc": 35},
    {"nazwa": "piwo", "cena": 6, "ilosc": 20},
    {"nazwa": "wino", "cena": 25, "ilosc": 8},
    {"nazwa": "szynka", "cena": 18, "ilosc": 10},
    {"nazwa": "parówki", "cena": 10, "ilosc": 14},
    {"nazwa": "jabłka", "cena": 4, "ilosc": 40},
    {"nazwa": "banany", "cena": 5, "ilosc": 30},
    {"nazwa": "pomarańcze", "cena": 6, "ilosc": 22},
    {"nazwa": "cytryny", "cena": 5, "ilosc": 18},
    {"nazwa": "ziemniaki", "cena": 3, "ilosc": 50},
    {"nazwa": "marchew", "cena": 3, "ilosc": 40},
    {"nazwa": "cebula", "cena": 2, "ilosc": 35},
    {"nazwa": "czosnek", "cena": 1, "ilosc": 15},
    {"nazwa": "ogórki", "cena": 5, "ilosc": 25},
    {"nazwa": "pomidory", "cena": 6, "ilosc": 28},
    {"nazwa": "lodówka", "cena": 1500, "ilosc": 2},
    {"nazwa": "telewizor", "cena": 2000, "ilosc": 1},
    {"nazwa": "smartfon", "cena": 1800, "ilosc": 3},
    {"nazwa": "laptop", "cena": 3500, "ilosc": 1},
    {"nazwa": "klawiatura", "cena": 150, "ilosc": 5},
    {"nazwa": "myszka", "cena": 80, "ilosc": 6},
    {"nazwa": "drukarka", "cena": 400, "ilosc": 2},
    {"nazwa": "tusz do drukarki", "cena": 100, "ilosc": 8},
    {"nazwa": "zeszyt", "cena": 6, "ilosc": 20},
    {"nazwa": "długopis", "cena": 2, "ilosc": 40},
    {"nazwa": "ołówek", "cena": 1, "ilosc": 35},
    {"nazwa": "linijka", "cena": 3, "ilosc": 15},
    {"nazwa": "plecak", "cena": 120, "ilosc": 4},
    {"nazwa": "rower", "cena": 1000, "ilosc": 2}
]
historia= ["Spredaż: rower, 1000, 1 sztuk" , "Zakup: plecak, 120, 2 sztuk" ]


saldo = 10000

print("Witaj w systemie księgowo-magazynowym!")

while True:
    print("Wybierz jedną z poniższych opjci podając numer 1-8:")
    komenda = input("""
    1. Salod
    2. Sprzedaż
    3. Zakup
    4. Konto
    5. Lista
    6. Magazyn
    7. Przegląd
    8. Koniec
    """)
    komenda = komenda.lower()

    match komenda:
        case "1":
            kwota = float(input("Pdaj kwotę o jaką chcesz zmienić saldo: \n"))
            if saldo + kwota < 0:
                print ("Saldo nie może być ujemne!")
            else:
                saldo +=kwota

        case "2":
            nazwa = input(f"Podaj produkt który chcesz zamówić: \n")
            produkt_znaleziony = False
            for produkt in produkty_startowe:
                if produkt.get("nazwa") == nazwa:
                    produkt["ilosc"] -= 1
                    cena = produkt["cena"]
                    saldo += cena
                    historia.append(f"Zakup: {produkt['nazwa']}, {produkt['cena']}, 1 sztuka")
                produkt_znaleziony = True
                break
            if not produkt_znaleziony:
                print("Tego produktu nie ma w asortymencie.")

        case "3":
            nazwa = input("Podaj nazwę produktu: \n")
            cena = float(input("Podaj cenę produktu: \n"))
            ilosc = int(input("Podaj ilość: \n"))
            koszt = cena * ilosc

            if saldo - koszt < 0:
                print("Nie możesz sprzedać produktu ponieważ saldo będzie ujemne.")
                historia.append(f"Próba zakupu: {nazwa}, {cena}, {ilosc} sztuk - nieudana.")
                continue
            else:
                saldo -= koszt

            produkt_znaleziony = False
            for produkt in produkty_startowe:
                if produkt["nazwa"] == nazwa:
                    produkt["ilosc"] += ilosc
                    produkt_znaleziony = True
                    break

            if not produkt_znaleziony:
                produkty_startowe.append({
                    "nazwa": nazwa,
                    "cena": cena,
                    "ilosc": ilosc
                })

            historia.append(f"Zakup: {nazwa}, {cena}, {ilosc} sztuk.")
            print(f"Zakupiono {ilosc} szt. produktu {nazwa} za {koszt} zł.")

        case "4":
            print(f"Bierzące środki na koncie: {saldo}")

        case "5":
            print(f"Całkowity stan magazynu: {produkty_startowe}")

        case "6":
            nazwa = input("Podaj nazwę produktu, aby sprawdzić jego stan w magazynie: \n")
            znaleziony = False

            for produkt in produkty_startowe:
                if produkt["nazwa"] == nazwa:
                    print(f"Produkt: {produkt['nazwa']}, Ilość: {produkt['ilosc']}, Cena: {produkt['cena']} zł")
                    znaleziony = True
                    break

            if not znaleziony:
                print(f"Produkt o nazwie '{nazwa}' nie znajduje się w magazynie.")

        case "7":
            od = input("Podaj waartość od (numer transakcji): ")
            do = input("Podaj wartość do (numer transakcji): ")
            if od:
                od=int(od)
            else:
                od = 0
            if do:
                do=int(do)
            else:
                do = len(historia)
            print(historia[od:do])

        case "8":
            print("Zakończono działanie programu.")
            break