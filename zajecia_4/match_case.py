zawod = input("Podaj mi swój zawód: ")
wiek = int(input("Podaj mi swój wiek: "))

match zawod:
    case "policjant":
        print(f"Do emerytury zostało Ci {45 - wiek} lat.")
    case "zolnierz":
        print(f"Do emerytury zostało Ci {50 - wiek} lat.")
    case "nauczyciel":
        print(f"Do emerytury zostało Ci {60 - wiek} lat.")
    case "praca biurowa":
        print(f"Do emerytury zostało Ci {65 - wiek} lat.")
    case "programista":
        print("Nie ma dla Ciebie emerytury")
    case _:
        print("Domyslna wartosc")
        print(f"Do twojej emerytury prawdopodobnie zostało Ci {65 - wiek} lat.")

liczba = int(input("Podaj mi liczbę: "))
