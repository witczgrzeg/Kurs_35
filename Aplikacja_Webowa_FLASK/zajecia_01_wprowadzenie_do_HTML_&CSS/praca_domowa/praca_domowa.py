from FileHandler import file_handler

produkty_startowe = file_handler.produkty
historia= file_handler.historia
saldo = file_handler.saldo

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

file_handler.produkty = produkty_startowe
file_handler.historia = historia
file_handler.saldo = saldo

file_handler.save_produkty_file()
file_handler.save_historia_file()
file_handler.save_saldo_file()
