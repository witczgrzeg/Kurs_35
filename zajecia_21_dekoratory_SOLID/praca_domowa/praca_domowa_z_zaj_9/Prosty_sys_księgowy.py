from FileHandler import file_handler
import logging

produkty = file_handler.produkty
historia = file_handler.historia
saldo = file_handler.saldo

print("Witaj w systemie księgowo-magazynowym!")

while True:
    print("Wybierz jedną z poniższych opcji podając numer 1-8:")
    komenda = input("""
    1. Saldo
    2. Sprzedaż
    3. Zakup
    4. Konto
    5. Lista
    6. Magazyn
    7. Przegląd
    8. Koniec
    """).strip().lower()

    match komenda:
        case "1":
            kwota = file_handler.get_float_input("Podaj kwotę o jaką chcesz zmienić saldo: \n")
            if kwota is None:
                continue
            if saldo + kwota < 0:
                print(" Saldo nie może być ujemne!")
            else:
                saldo += kwota
                print(f" Saldo zostało zmienione. Nowe saldo: {saldo}")

        case "2":
            nazwa = input("Podaj nazwę produktu do sprzedaży: \n")
            produkt_znaleziony = False
            for produkt in produkty:
                if produkt.get("nazwa") == nazwa:
                    if produkt["ilosc"] <= 0:
                        print(" Produkt jest niedostępny.")
                        logging.warning(f"Brak produktu przy sprzedaży: {nazwa}")
                        produkt_znaleziony = True
                        break
                    produkt["ilosc"] -= 1
                    saldo += produkt["cena"]
                    historia.append(f"Sprzedaż: {produkt['nazwa']}, {produkt['cena']}, 1 szt.")
                    print(f" Sprzedano 1 szt. {nazwa}")
                    produkt_znaleziony = True
                    break
            if not produkt_znaleziony:
                print(" Nie znaleziono produktu.")
                logging.warning(f"Nieznany produkt przy sprzedaży: {nazwa}")

        case "3":
            nazwa = input("Podaj nazwę produktu do zakupu: \n")
            cena = file_handler.get_float_input("Podaj cenę produktu: \n")
            ilosc = file_handler.get_int_input("Podaj ilość: \n")
            if cena is None or ilosc is None:
                continue
            koszt = cena * ilosc
            if saldo - koszt < 0:
                print(" Saldo niewystarczające.")
                historia.append(f"Próba zakupu: {nazwa}, {cena}, {ilosc} szt. - nieudana.")
                logging.warning(f"Próba zakupu ponad saldo: {nazwa}, {koszt}")
                continue
            saldo -= koszt
            for produkt in produkty:
                if produkt["nazwa"] == nazwa:
                    produkt["ilosc"] += ilosc
                    break
            else:
                produkty.append({"nazwa": nazwa, "cena": cena, "ilosc": ilosc})
            historia.append(f"Zakup: {nazwa}, {cena}, {ilosc} szt.")
            print(f" Zakupiono {ilosc} szt. {nazwa} za {koszt} zł")

        case "4":
            print(f" Bieżące saldo: {saldo}")

        case "5":
            print(" Zawartość magazynu:")
            for produkt in produkty:
                print(f"- {produkt['nazwa']}: {produkt['ilosc']} szt., cena: {produkt['cena']} zł")

        case "6":
            nazwa = input("Podaj nazwę produktu do sprawdzenia: \n")
            for produkt in produkty:
                if produkt["nazwa"] == nazwa:
                    print(f" Produkt: {produkt['nazwa']}, Ilość: {produkt['ilosc']}, Cena: {produkt['cena']} zł")
                    break
            else:
                print(" Nie znaleziono produktu.")
                logging.warning(f"Sprawdzenie nieistniejącego produktu: {nazwa}")

        case "7":
            od = file_handler.get_int_input("Podaj numer transakcji OD: ")
            do = file_handler.get_int_input("Podaj numer transakcji DO: ")
            if od is None or do is None:
                continue
            print(" Historia transakcji:")
            for wpis in historia[od:do]:
                print("-", wpis)

        case "8":
            print(" Zamykanie programu.")
            break

        case _:
            print(" Nieprawidłowa opcja.")
            logging.info(f"Nieznana komenda: {komenda}")

file_handler.produkty = produkty
file_handler.historia = historia
file_handler.saldo = saldo

file_handler.save_produkty_file()
file_handler.save_historia_file()
file_handler.save_saldo_file()
