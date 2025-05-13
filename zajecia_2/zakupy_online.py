'''
Zakupy online - rabaty

Wczytaj od użytkownika:
- czy zamówienie przekracza 100 zł (tak/nie),
- czy jest klientem VIP (tak/nie),
- czy kupił produkt promocyjny (tak/nie).

Rabat:
- 15% jeśli zamówienie >100 zł lub VIP,
- dodatkowe 5% jeśli produkt promocyjny.

Wyświetl "Twój rabat wynosi X%" bez użycia ifów.
'''

zamowienie = float(input("Podaj cenę swojego zamówienia: "))


vip = input("Czy jesteś klientem VIP? (tak/nie): ")
vip = vip.lower()

promocja = input("Czy kupiłeś produkt promocyjny? (tak/nie): ")
promocja = promocja.lower()

zamowienie_powyzej_100 = zamowienie >= 100
klient_vip = vip == "tak"
produkt_promocyjny = promocja == "tak"

rabat = 0.15 * (zamowienie_powyzej_100 or klient_vip) + 0.05 * produkt_promocyjny

print(f"Twoje zamówienie po rabatowaniu wynosi: {zamowienie * (1 - rabat)}")
