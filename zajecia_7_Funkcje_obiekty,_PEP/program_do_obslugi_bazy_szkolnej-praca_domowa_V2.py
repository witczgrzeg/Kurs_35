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

def dodaj_nauczyciela_lub_wychowawcę(imie, nazwisko, klasa, przedmiot, stanowisko):
    nauczyciel = "nauczyciel"(imie, nazwisko, klasa, przedmiot, stanowisko)
    lista["pracownik_szkoly"].append(nauczyciel)
    print(f"Dodano pracownika: {stanowisko}, imię {imie} {nazwisko}, do klasy {klasa}")

def dodaj_ucznia(imie, nazwisko, klasa):
    uczen = uczen_szkoly(imie, nazwisko, klasa)
    lista["uczen_szkoly"].append(uczen)
    print(f"Dodano : {imie} {nazwisko}, klasa {klasa}")
def klasy



lista = {
    "nauczyciel": [
        nauczyciel("Tomasz", "Wrona", "1A", "Fizyka", "Nauczyciel"),
        nauczyciel("Monika", "Zielińska", "1B", "Chemia", "Nauczyciel"),
        nauczyciel("Karolina", "Wiśniewska", "1C", "Język angielski", "Nauczyciel"),
        nauczyciel("Marek", "Nowicki", "1A", "Wychowanie fizyczne", "Nauczyciel")
    ],
    "wychowawca":[
        wychowawca("Alicja", "Kaczmarek", "0", "Historia", "Dyrektor"),
        wychowawca("Agnieszka", "Piotrowska", "1A", "Matematyka", "Wychowawca"),
        wychowawca("Rafał", "Sadowski", "1B", "Polski", "Wychowawca"),
        wychowawca("Beata", "Jankowska", "1C", "Biologia", "Wychowawca"),
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
    \n""")
    if komenda.strip().lower() in ("1", "Utwórz", "Utworz"):
        pass

    match komenda:
        case "1":
            print("Wybierz jedną z poniższych opcji (wybierając 1-4)")
            utworz = input("""
            1. Uczeń
            2. Nauczyciel
            3. Wychowawca
            4. Koniec
            \n""")

            if utworz.strip().lower() in ("1", "Uczeń", "Uczen"):
                imie = input("Podaj imię ucznia:\n")
                nazwisko = input("Podaj nazwisko ucznia:\n")
                klasa = input("Do której klasy należy:\n")
                nowy_uczen = uczen_szkoly(imie, nazwisko, klasa)
                lista["uczen_szkoly"].append(nowy_uczen)

            elif utworz.strip().lower() in ("2", "Nauczyciel",):
                imie = input("Podaj imię:\n")
                nazwisko = input("Podaj Nazwisko:\n")
                klasa = input ("Podaj klasę w której uczy:\n")
                przedmiot = input("Czego uczy (matematyka, biologia:\n")
                stanowisko = "Nauczyciel"
                nowy_nauczyciel = pracownik_szkoly(imie, nazwisko, klasa, przedmiot, stanowisko)
                lista["pracownik_szkoly"].append(nowy_nauczyciel)
            elif utworz.strip().lower() in ("3", "wychowawca"):
                imie = input("Podaj imię:\n")
                nazwisko = input("Podaj Nazwisko:\n")
                klasa = input("Podaj klasę w której jest wychowawcą:\n")
                przedmiot = input("Czego uczy (matematyka, biologia:\n")
                stanowisko = "Wychowawca"
                nowy_nauczyciel = pracownik_szkoly(imie, nazwisko, klasa, przedmiot, stanowisko)
                lista["pracownik_szkoly"].append(nowy_nauczyciel)


        case "2":
            print("Wybierz jedną z poniższych opcji (wybierając 1-5)")
            zarzadzaj = input("""
                       1. Klasa
                       2. Uczeń
                       3. Nauczyciel
                       4. Wyhowawca
                       5. Koniec
                       \n""")
            if zarzadzaj.strip().lower() in ("1", "Klasa", "klasa"):
                pass
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
            print(lista)
            print("Zakończono działanie programu.")
            break