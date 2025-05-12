print("sklep zabka")
print("witaj")

nazwa_produktu = input("podaj nazwe produktu: ")
cena_produktu = float(input("podaj cena produktu: "))
age_klienta = int(input("podaj wiek klienta: "))

print(f"kupiles {nazwa_produktu} o cenie: {cena_produktu} zł")

if age_klienta >= 18:
    print("warunek wieku został spełniony")
