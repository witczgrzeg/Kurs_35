
def main():
    konto = 0.0
    magazyn = {}
    historia = []

    def wypisz_komendy():
        print("\nDostępne komendy:")
        print("saldo\nsprzedaż\nzakup\nkonto\nlista\nmagazyn\nprzegląd\nkoniec")

    while True:
        wypisz_komendy()
        komenda = input("\nWprowadź komendę: ").strip().lower()

        if komenda == "saldo":
            try:
                kwota = float(input("Podaj kwotę (może być ujemna): "))
                konto += kwota
                historia.append(("saldo", kwota))
            except ValueError:
                print("Nieprawidłowa kwota.")

        elif komenda == "sprzedaż":
            produkt = input("Podaj nazwę produktu: ").strip()
            if produkt not in magazyn:
                print("Produkt nie istnieje w magazynie.")
                continue
            try:
                cena = float(input("Podaj cenę sprzedaży: "))
                ilosc = int(input("Podaj liczbę sztuk: "))
                if ilosc <= 0 or cena < 0:
                    print("Błędna ilość lub cena.")
                    continue
                if magazyn[produkt][0] < ilosc:
                    print("Brak wystarczającej liczby sztuk w magazynie.")
                    continue
                magazyn[produkt][0] -= ilosc
                konto += cena * ilosc
                historia.append(("sprzedaż", produkt, cena, ilosc))
            except ValueError:
                print("Nieprawidłowe dane.")

        elif komenda == "zakup":
            produkt = input("Podaj nazwę produktu: ").strip()
            try:
                cena = float(input("Podaj cenę zakupu: "))
                ilosc = int(input("Podaj liczbę sztuk: "))
                if cena < 0 or ilosc <= 0:
                    print("Cena i ilość muszą być dodatnie.")
                    continue
                koszt = cena * ilosc
                if konto < koszt:
                    print("Brak środków na zakup.")
                    continue
                konto -= koszt
                if produkt in magazyn:
                    magazyn[produkt][0] += ilosc
                else:
                    magazyn[produkt] = [ilosc, cena]
                historia.append(("zakup", produkt, cena, ilosc))
            except ValueError:
                print("Nieprawidłowe dane.")

        elif komenda == "konto":
            print(f"Aktualny stan konta: {konto:.2f}")

        elif komenda == "lista":
            print("Stan magazynu:")
            for produkt, (ilosc, cena) in magazyn.items():
                print(f"{produkt}: {ilosc} szt., cena: {cena:.2f}")

        elif komenda == "magazyn":
            nazwa = input("Podaj nazwę produktu: ").strip()
            if nazwa in magazyn:
                print(f"{nazwa}: {magazyn[nazwa][0]} szt., cena: {magazyn[nazwa][1]:.2f}")
            else:
                print("Produkt nie istnieje w magazynie.")

        elif komenda == "przegląd":
            try:
                od = input("Od indeksu (enter dla początku): ")
                do = input("Do indeksu (enter dla końca): ")

                start = int(od) if od else 0
                end = int(do) + 1 if do else len(historia)

                if start < 0 or end > len(historia):
                    print(f"Zakres poza listą. Zapisanych komend: {len(historia)}")
                    continue

                for i, wpis in enumerate(historia[start:end], start=start):
                    print(f"{i}: {wpis}")
            except ValueError:
                print("Nieprawidłowy zakres.")

        elif komenda == "koniec":
            print("Zakończono działanie programu.")
            break

        else:
            print("Nieznana komenda.")

if __name__ == "__main__":
    main()
