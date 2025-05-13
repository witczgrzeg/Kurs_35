# imie = "Michal"
# print(imie)

# print("Symulacja sklepu żabka: ")
# print("Witaj w sklepie Żabka!")
#
# nazwa_produktu = input("Podaj nazwę produktu: ")
# cena_produktu = float(input("Podaj cenę produktu: "))

# if wiek_klienta >= 18:
#     print("Warunek wieku został spełniony.")
#     print("Dalej jestesmy w bloku kodu")
#
# if wiek_klienta < 18:
#     print("Nie możesz kupować produktów dla pełnoletnich.")
#
# print("jestesmy poza instrukcja warunkową!")
#
# if wiek_klienta >= 18:
#     print("Możesz kupić produkt!")
# else:
#     print("Nie możesz kupić produktu!")
#
# if nazwa_produktu.lower() == "piwo" or nazwa_produktu.lower() == "papierosy" or nazwa_produktu.lower() == "energetyk" or nazwa_produktu.lower() == "alkohol wysokoprocentowy":
#     print("Ten produkt jest przeznaczony dla osób pełnoletnich.")
#     wiek_klienta = int(input("Podaj swój wiek: "))
#     if wiek_klienta >= 18:
#         print("Masz 18 lat lub więcej. Możesz kupić ten produkt.")
#         print(f"Kupiłeś produkt {nazwa_produktu} w cenie {cena_produktu} zł.")
#     else:
#         print("Nie masz 18 lat. Nie możesz kupić tego produktu.")
# else:
#     print("Ten produkt nie wymaga podawania wieku.")
#     print(f"Kupiłeś produkt {nazwa_produktu} w cenie {cena_produktu} zł.")



zawod = input("Podaj swój zawód: ")
wiek = int(input("Podaj swój wiek: "))

if zawod == "policjant":
    print(f"Do emerytury zostało Ci {45 - wiek} lat.")
elif zawod == "zolnierz":
    print(f"Do emerytury zostało Ci {50 - wiek} lat.")
elif zawod == "nauczyciel":
    print(f"Do emerytury zostało Ci {60 - wiek} lat.")
elif zawod == "praca biurowa":
    print(f"Do emerytury zostało Ci {65 - wiek} lat.")
elif zawod == "programista":
    print("Nie ma emerytury dla programistów!")
else:
    print(f"Do twojej emerytury prawdopodobnie zostało Ci {65 - wiek} lat.")


################
"""
warunek logiczny - wyrazenie, ktore zwroci wartość typu boolean (True/False)
if {warunek logiczny}:
    {blok kodu}
elif {warunek logiczny}:
    {blok kodu}
else:
    {blok kodu}
"""
