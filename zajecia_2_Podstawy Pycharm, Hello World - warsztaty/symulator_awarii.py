"""
Symulator awarii systemu

Wczytaj od użytkownika:
- czy serwer odpowiada (tak/nie),
- czy baza danych działa (tak/nie),
- czy aplikacja webowa jest dostępna (tak/nie).

Awaria:
- Krytyczna: serwer nie działa i baza nie działa.
- Częściowa: serwer lub baza lub aplikacja nie działa.

Wyświetl:
- "Natychmiastowa interwencja!",
- "Awaria częściowa - sprawdź system",
- "System działa poprawnie".
"""
serwer_awaria = input("Serwer nie odpowiada? (tak/nie): ")
serwer_awaria = serwer_awaria.lower()

baza_awaria = input("Baza danych nie działa? (tak/nie): ")
baza_awaria = baza_awaria.lower()

aplikacja_awaria = input("Aplikacja webowa jest dostępna? (tak/nie): ")
aplikacja_awaria = aplikacja_awaria.lower()

print("Natychmiastowa interwencja" * (serwer_awaria == "tak" and baza_awaria == "tak") + " Awaria częściowa - sprawdź system"
      * (serwer_awaria == "tak" or baza_awaria == "tak" or aplikacja_awaria == "tak")
      + "System działa poprawnie" * (serwer_awaria == "nie" and baza_awaria == "nie" and aplikacja_awaria == "nie"))