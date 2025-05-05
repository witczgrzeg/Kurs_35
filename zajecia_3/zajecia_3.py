print("witaj w sklepie zabka")

nazwa_prod = input("Podaj nazwę produkt: \n")
cena_prod = float(input("Podaj cenaj produkt: \n"))
wiek_klienta= int(input("podaj sówj wiek: \n"))

print(f"kupiłeś produkt {nazwa_prod} o cenie: {cena_prod} zł\n")

if wiek_klienta >=18:
    print("warunek wieku został spełniony")

if wiek_klienta < 18:
    print("Nie możesz kupować porduktów dla pełnoletnich")