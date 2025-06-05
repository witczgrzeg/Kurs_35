"""

Utwórz program do zarządzania bazą szkolną. Istnieje możliwość tworzenia trzech typów użytkowników (uczeń, nauczyciel, wychowawca) a także zarządzania nimi.

Po uruchomieniu programu można wpisać jedną z następujących komend: utwórz, zarządzaj, koniec.

Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
Polecenie "koniec" - Kończy działanie aplikacji.

Proces tworzenia użytkowników:

Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia (jako jedna zmienna, można pobrać je jako dwie zmienne, jeżeli zostanie to poprawnie obsłużone) oraz nazwę klasy (np. "3C")
Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela (jako jedna zmienna, labo dwie, jeżeli zostanie to poprawnie obsłużone), nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas, które prowadzi nauczyciel, aż do otrzymania pustej linii.
Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy (jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone), a także nazwę prowadzonej klasy.
Polecenie "koniec" - Wraca do pierwszego menu.

Proces zarządzania użytkownikami:

Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C") program ma wypisać wszystkich uczniów, którzy należą do tej klasy, a także wychowawcę tejże klasy.
Polecenie "uczeń" - Należy pobrać imię i nazwisko uczenia, program ma wypisać wszystkie lekcje, które ma uczeń a także nauczycieli, którzy je prowadzą.
Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela, program ma wypisać wszystkie klasy, które prowadzi nauczyciel.
Polecenie "wychowawca" - Należy pobrać imię i nazwisko nauczyciela, a program ma wypisać wszystkich uczniów, których prowadzi wychowawca.
Polecenie "koniec" - Wraca do pierwszego menu.

"""



class pracownik_szkoly:
    def __init__(self, imie, nazwisko, klasa, przedmiot, stanowisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa
        self.przedmiot = przedmiot
        self.stanowisko = stanowisko

    def __repr__(self):
        return f"{self.imie} {self.nazwisko}, {self.klasa}, {self.przedmiot}, {self.stanowisko}"

class uczen_szkoly:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} ({self.klasa})"

class klasa:
    def __init__(self, klasa):
        self.klasa = klasa


    def __repr__(self):
        return f"{self.klasa}"

lista = {
    "pracownik_szkoly": [
        pracownik_szkoly("Alicja", "Kaczmarek", "0", "Historia", "Dyrektor"),
        pracownik_szkoly("Agnieszka", "Piotrowska", "1A", "Matematyka", "Wychowawca"),
        pracownik_szkoly("Rafał", "Sadowski", "1B", "Polski", "Wychowawca"),
        pracownik_szkoly("Beata", "Jankowska", "1C", "Biologia", "Wychowawca"),
        pracownik_szkoly("Tomasz", "Wrona", "1A", "Fizyka", "Nauczyciel"),
        pracownik_szkoly("Monika", "Zielińska", "1B", "Chemia", "Nauczyciel"),
        pracownik_szkoly("Karolina", "Wiśniewska", "1C", "Język angielski", "Nauczyciel"),
        pracownik_szkoly("Marek", "Nowicki", "1A", "Wychowanie fizyczne", "Nauczyciel")
    ],
    "uczen_szkoly": [
        uczen_szkoly("Jan", "Kowalski", "1A"),
        uczen_szkoly("Anna", "Nowak", "1A"),
        uczen_szkoly("Tomasz", "Wiśniewski", "1A"),
        uczen_szkoly("Kacper", "Wójcik", "1A"),
        uczen_szkoly("Zofia", "Kamińska", "1A"),
        uczen_szkoly("Mikołaj", "Dąbrowski", "1A"),
        uczen_szkoly("Oliwia", "Nowak", "1A"),
        uczen_szkoly("Tomasz", "Lis", "1A"),
        uczen_szkoly("Wiktor", "Grabowski", "1B"),
        uczen_szkoly("Julia", "Pawlak", "1B"),
        uczen_szkoly("Mateusz", "Michalak", "1B"),
        uczen_szkoly("Emilia", "Baran", "1B"),
        uczen_szkoly("Antoni", "Witkowski", "1B"),
        uczen_szkoly("Aleksandra", "Kaczmarek", "1B"),
        uczen_szkoly("Bartłomiej", "Czarnecki","1B"),
        uczen_szkoly("Filip","Kowalczyk","1B"),
        uczen_szkoly("Lena","Zawadzka","1B"),
        uczen_szkoly("Michał", "Nowicki", "1C"),
        uczen_szkoly("Martyna", "Szymańska", "1C"),
        uczen_szkoly("Jakub", "Woźniak", "1C"),
        uczen_szkoly("Zuzanna", "Adamska", "1C"),
        uczen_szkoly("Szymon", "Rutkowski", "1C"),
        uczen_szkoly("Julia", "Krawczyk", "1C")
    ],
    "klasy": [
        klasa("1A"),
        klasa("1B"),
        klasa("1C")
    ]
}

# Jeśli chcesz ładnie wydrukować:
for kategoria, obiekty in lista.items():
    print(f"\n{kategoria.upper()}:")
    for obiekt in obiekty:
        print(f" - {obiekt}")

#
#

#     },
#     {
#         "stanowisko": "Wychowarca",
#         "imie": "Rafał",
#         "nazwisko": "Sadowski",
#         "klasa": "Pierwsza",
#         "numer": "1B"
#     },
#     {
#         "stanowisko": "Wychowarca",
#         "imie": "Beata",
#         "nazwisko": "Jankowska",
#         "klasa": "Pierwsza",
#         "numer": "1C"
#     }
# ]
#
# #
# # def dodaj_uzytkownika(stanowisko, imie, nazwisko, klasa, numer):
# #     uzytkownik = {
# #         "stanowisko": stanowisko,
# #         "imie": imie,
# #         "nazwisko": nazwisko,
# #         "klasa": klasa,
# #         "numer": numer
# #     }
# #     lista_uzytkownikow.append(uzytkownik)
# #
# #     print(f"dodano: stanowisko:{stanowisko}, imię {imie} {nazwisko}, do {klasa} {numer}")
# #
# # dodaj_uzytkownika("uczen", "XjanuszX", "XkowalX", "Trzecia", "3B")
# # dodaj_uzytkownika("nauczyciel", "Jan", "Kowalski","Pierwsza", "1A")
# # for uzytkownik in lista_uzytkownikow:
# #     print(uzytkownik)
# #
# # print("Witaj w systemie bazy szkolnej")
# #
# # while True:
# #
# #     print("Wybierz jedną z poniższych opcji (wybierając 1-3)")
# #     komenda = input("""
# #     1. Utwórz
# #     2. Zarządzaj
# #     3. Koniec
# #     \n""")
# #     komenda = komenda.lower()
# #
# #     match komenda:
# #         case "1":
# #             print("Wybierz jedną z poniższych opcji (wybierając 1-4)")
# #             utworz = input("""
# #             1. Uczeń
# #             2. Nauczyciel
# #             3. Wychowawca
# #             4. Koniec
# #             """)
# #             match utworz:
# #                 case "1":
# #                    print ("wpisz coś")
# #
# #         case "2":
# #             print("Wybierz jedną z poniższych opcji (wybierając 1-5)")
# #             zarzadzaj = input("""
# #                        1. Klasa
# #                        2. Uczeń
# #                        3. Nauczyciel
# #                        4. Wyhowawca
# #                        5. Koniec
# #                        """)
# #             match zarzadzaj:
# #                 case "1":
# #                     for klasa in lista_uzytkownikow:
# #                         if klasa["klasa"] == uzytkownik:
# #                             print(klasa)
# #
# #         case "3":
# #             print("Zakończono działanie programu.")
# #             break