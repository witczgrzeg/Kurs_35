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

class nauczyciel:
    def __init__(self, imie, nazwisko, klasa, przedmiot, stanowisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa
        self.przedmiot = przedmiot
        self.stanowisko = "Nauczyciel"
    def __repr__(self):
        return f"{self.imie} {self.nazwisko}, {self.klasa}, {self.przedmiot}, {self.stanowisko}"
class wychowawca:
    def __init__(self, imie, nazwisko, klasa, przedmiot, stanowisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa
        self.przedmiot = przedmiot
        self.stanowisko = "Wychowawca"
    def __repr__(self):
        return f"{self.imie} {self.nazwisko}, {self.klasa}, {self.przedmiot}, {self.stanowisko}"
class uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa
    def __repr__(self):
        return f"{self.imie} {self.nazwisko} ({self.klasa})"

def dodaj_nauczyciela(imie, nazwisko, klasa, przedmiot):
    nowy_nauczyciel = nauczyciel (imie, nazwisko, klasa, przedmiot)
    lista["nauczyciele"].append(nowy_nauczyciel)
def dodaj_wychowawce(imie, nazwisko, klasa, przedmiot):
    nowy_wychowawca = wychowawca (imie, nazwisko, klasa, przedmiot)
    lista["wychowawcy"].append(nowy_wychowawca)
def dodaj_ucznia(imie, nazwisko, klasa):
    nowy_uczen = uczen(imie, nazwisko, klasa)
    lista["uczniowie"].append(nowy_uczen)




lista = {
    "nauczyciele": [
        nauczyciel("Tomasz", "Wrona", "1A", "Fizyka", "Nauczyciel"),
        nauczyciel("Monika", "Zielińska", "1B", "Chemia", "Nauczyciel"),
        nauczyciel("Karolina", "Wiśniewska", "1C", "Język angielski", "Nauczyciel"),
        nauczyciel("Marek", "Nowicki", "1A", "Wychowanie fizyczne", "Nauczyciel")
    ],
    "wychowawcy":[
        wychowawca("Alicja", "Kaczmarek", "0", "Historia", "Dyrektor"),
        wychowawca("Agnieszka", "Piotrowska", "1A", "Matematyka", "Wychowawca"),
        wychowawca("Rafał", "Sadowski", "1B", "Polski", "Wychowawca"),
        wychowawca("Beata", "Jankowska", "1C", "Biologia", "Wychowawca"),
                  ],
    "uczniowie": [
        uczen("Jan", "Kowalski", "1A"),
        uczen("Anna", "Nowak", "1A"),
        uczen("Tomasz", "Wiśniewski", "1A"),
        uczen("Kacper", "Wójcik", "1A"),
        uczen("Zofia", "Kamińska", "1A"),
        uczen("Mikołaj", "Dąbrowski", "1A"),
        uczen("Oliwia", "Nowak", "1A"),
        uczen("Tomasz", "Lis", "1A"),
        uczen("Wiktor", "Grabowski", "1B"),
        uczen("Julia", "Pawlak", "1B"),
        uczen("Mateusz", "Michalak", "1B"),
        uczen("Emilia", "Baran", "1B"),
        uczen("Antoni", "Witkowski", "1B"),
        uczen("Aleksandra", "Kaczmarek", "1B"),
        uczen("Bartłomiej", "Czarnecki", "1B"),
        uczen("Filip", "Kowalczyk", "1B"),
        uczen("Lena", "Zawadzka", "1B"),
        uczen("Michał", "Nowicki", "1C"),
        uczen("Martyna", "Szymańska", "1C"),
        uczen("Jakub", "Woźniak", "1C"),
        uczen("Zuzanna", "Adamska", "1C"),
        uczen("Szymon", "Rutkowski", "1C"),
        uczen("Julia", "Krawczyk", "1C")
    ]
}

# # Jeśli chcesz ładnie wydrukować:
# for kategoria, obiekty in lista.items():
#     print(f"\n{kategoria.upper()}:")
#     for obiekt in obiekty:
#         print(f" - {obiekt}")
#
# dodaj_ucznia("uczen", "XjanuszX", "3B")
# dodaj_uzytkownika("Jan", "Kowalski", "1A","WOS", "Nauczyciel")




print("Witaj w systemie bazy szkolnej")

while True:

    print("Wybierz jedną z poniższych opcji (wybierając 1-3)")
    komenda = input("""
    1. Utwórz
    2. Zarządzaj
    3. Koniec
    \n""").strip().lower()

    match komenda:
        case "1":
            print("Wybierz jedną z poniższych opcji (wybierając 1-4)")
            utworz = input("""
            1. Uczeń
            2. Nauczyciel
            3. Wychowawca
            4. Koniec
            \n""").strip().lower()

            if utworz.strip().lower() in ("1", "Uczeń", "Uczen", "uczen", "uczeń"):
                imie = input("Podaj imię ucznia:\n")
                nazwisko = input("Podaj nazwisko ucznia:\n")
                klasa = input("Do której klasy należy:\n")
                add_uczen = uczen(imie, nazwisko, klasa)
                lista["uczniowie"].append(add_uczen)

            elif utworz.strip().lower() in ("2", "Nauczyciel", "nauczyciel",):
                imie = input("Podaj imię:\n")
                nazwisko = input("Podaj Nazwisko:\n")
                klasa = input ("Podaj klasę w której uczy:\n")
                przedmiot = input("Czego uczy (matematyka, biologia:\n")
                stanowisko = "Nauczyciel"
                add_nauczyciel = nauczyciel(imie, nazwisko, klasa, przedmiot, stanowisko)
                lista["nauczyciele"].append(add_nauczyciel)

            elif utworz.strip().lower() in ("3", "wychowawca", "Wychowawca"):
                imie = input("Podaj imię:\n")
                nazwisko = input("Podaj Nazwisko:\n")
                klasa = input("Podaj klasę w której jest wychowawcą:\n")
                przedmiot = input("Czego uczy (matematyka, biologia:\n")
                stanowisko = "Wychowawca"
                add_wychowawca = wychowawca(imie, nazwisko, klasa, przedmiot, stanowisko)
                lista["wychowawcy"].append(add_wychowawca)

            else:
                print("Nie wybrano poprawnej opcji. Spróbuj jeszcze raz.")


        case "2":
            print("Wybierz jedną z poniższych opcji (wybierając 1-5)")
            zarzadzaj = input("""
                       1. Klasa
                       2. Uczeń
                       3. Nauczyciel
                       4. Wyhowawca
                       5. Koniec
                       \n""")
            match zarzadzaj:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
        case "3":
            # Jeśli chcesz ładnie wydrukować:
            for kategoria, obiekty in lista.items():
                print(f"\n{kategoria.upper()}:")
                for obiekt in obiekty:
                    print(f" - {obiekt}")

            print("Zakończono działanie programu.")
            break