#### Zajęcia_2 ####

"""
A. bramki logiczne

1. pierwsze wyrażenie (prawda/fausz)
2. drugie wyrażenie (prawda/fausz)


            #and# - oba warunki muszą być spełnione
        prawda      fausz
prawda  true = 1    false = 0
fausz   false = 0   false = 0

            # or # tylko jedno musi być prawdziwe

        prawda      fausz
prawda  true = 1    true = 1
fausz   true = 1    false = 0

python domyslnie przyjmuje wartosc 0 jako false a 1 jako true

"""

#Przykład:
#wiek = int(input("Podaj swój wiek: "))
#plec = input("Podaj plec: ")
#czy_moge_glosowac = wiek >= 25 or plec == "mężczyzna"
#print(czy_moge_glosowac)


#Zadanie 1 - wypożyczalnia filmów
wiek = int(input("Podaj swój wiek:"))
zgoda = input("czy jest zgoda rodziców: ")
zgoda = zgoda.lower()

zgoda_pot = zgoda == "tak"
ma_dos_18 = wiek >= 18
dos_13 = wiek>=13 or zgoda_pot
tylko_bajki = wiek >13

print(f"user ma {wiek} lat")
print(f"user ma dostęp do 18+: {ma_dos_18}")
print(f"user ma dostęp do 13+: {dos_13}")
print(f"user ma dostęp tylko do bajek: {tylko_bajki}")
"""
wynik:

czy jest zgoda rodziców: nie
user ma 19 lat
user ma dostęp do 18+: True
user ma dostęp do 13+: True
user ma dostęp tylko do bajek: True

"""

# print (f"string": {bramka_logiczna} da print true albo false

# Zadanie 2

"""
Zakupy online - rabaty 

"""

print("Witamy w naszym sklepie")

zamowienie = input("Czy zamówienie przekracza 100zł? (tak/nie): ")
zamowienie = zamowienie.lower()
VIP = input("Czy jesteś klientem VIP? (tak/nie): ")
VIP = VIP.lower()

promocja = input("Czy kupiłeś produkt promocyjny? (tak/nie): ")
promocja = promocja.lower()

zamowienie_pow_100 = zamowienie =="tak"
klient_vip = VIP =="tak"
produkt_promocyjny = promocja == "tak"

rabat = 0.15 * (zamowienie_pow_100) or klient_vip * 0.05 + produkt_promocyjny
print(f"twój rabat wynosi {rabat * 100} %")


#### Zajęcia_3 ####
"""
warunek logiczny - wyrazenie, ktore zwroci wartość typu boolean (True/False)
if {warunek logiczny}:
    {blok kodu}
elif {warunek logiczny}:
    {blok kodu}
else:
    {blok kodu}
"""