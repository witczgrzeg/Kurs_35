class Nauczyciel:
    def __init__(self, imie, nazwisko, klasy, przedmiot):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasy = klasy
        self.przedmiot = przedmiot
        self.stanowisko = "Nauczyciel"

    def __repr__(self):
        klasy_str = ", ".join(self.klasy) if self.klasy else "Brak klas"
        return f"{self.imie} {self.nazwisko}, {klasy_str}, {self.przedmiot}, {self.stanowisko}"

class Wychowawca:
    def __init__(self, imie, nazwisko, klasy, przedmiot, stanowisko=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasy = klasy
        self.przedmiot = przedmiot
        if stanowisko == "Dyrektor":
            self.stanowisko = stanowisko
        else:
            self.stanowisko = "Wychowawca"

    def __repr__(self):
        klasy_str = ", ".join(self.klasy) if self.klasy else "Brak klas"
        return f"{self.imie} {self.nazwisko}, {klasy_str}, {self.przedmiot}, {self.stanowisko}"

class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

    def __repr__(self):
        return f"{self.imie} {self.nazwisko}, klasa {self.klasa}"

def dodaj_nauczyciela(imie, nazwisko, klasy, przedmiot):
    nowy_nauczyciel = Nauczyciel(imie, nazwisko, klasy, przedmiot)
    lista["nauczyciele"].append(nowy_nauczyciel)

def dodaj_wychowawce(imie, nazwisko, klasy, przedmiot, stanowisko=None):
    nowy_wychowawca = Wychowawca(imie, nazwisko, klasy, przedmiot, stanowisko)
    lista["wychowawcy"].append(nowy_wychowawca)

def dodaj_ucznia(imie, nazwisko, klasa):
    nowy_uczen = Uczen(imie, nazwisko, klasa)
    lista["uczniowie"].append(nowy_uczen)


lista = {
    "nauczyciele": [
        Nauczyciel("Tomasz", "Wrona", ["1A"], "Fizyka"),
        Nauczyciel("Monika", "Zielińska", ["1B"], "Chemia"),
        Nauczyciel("Karolina", "Wiśniewska", ["1C"], "Język angielski"),
        Nauczyciel("Marek", "Nowicki", ["1A"], "Wychowanie fizyczne")
    ],
    "wychowawcy": [
        Wychowawca("Alicja", "Kaczmarek", [], "Historia", "Dyrektor"),
        Wychowawca("Agnieszka", "Piotrowska", ["1A"], "Matematyka"),
        Wychowawca("Rafał", "Sadowski", ["1B"], "Polski"),
        Wychowawca("Beata", "Jankowska", ["1C"], "Biologia"),
    ],
    "uczniowie": [
        Uczen("Jan", "Kowalski", "1A"),
        Uczen("Anna", "Nowak", "1A"),
        Uczen("Tomasz", "Wiśniewski", "1A"),
        Uczen("Kacper", "Wójcik", "1A"),
        Uczen("Zofia", "Kamińska", "1A"),
        Uczen("Mikołaj", "Dąbrowski", "1A"),
        Uczen("Oliwia", "Nowak", "1A"),
        Uczen("Tomasz", "Lis", "1A"),
        Uczen("Wiktor", "Grabowski", "1B"),
        Uczen("Julia", "Pawlak", "1B"),
        Uczen("Mateusz", "Michalak", "1B"),
        Uczen("Emilia", "Baran", "1B"),
        Uczen("Antoni", "Witkowski", "1B"),
        Uczen("Aleksandra", "Kaczmarek", "1B"),
        Uczen("Bartłomiej", "Czarnecki", "1B"),
        Uczen("Filip", "Kowalczyk", "1B"),
        Uczen("Lena", "Zawadzka", "1B"),
        Uczen("Michał", "Nowicki", "1C"),
        Uczen("Martyna", "Szymańska", "1C"),
        Uczen("Jakub", "Woźniak", "1C"),
        Uczen("Zuzanna", "Adamska", "1C"),
        Uczen("Szymon", "Rutkowski", "1C"),
        Uczen("Julia", "Krawczyk", "1C")
    ]
}

def wyswietl_klase(nazwa_klasy):
    uczniowie = [uczen for uczen in lista["uczniowie"] if uczen.klasa == nazwa_klasy]
    wychowawcy = [wych for wych in lista["wychowawcy"] if nazwa_klasy in wych.klasy]

    print(f"\nUczniowie klasy {nazwa_klasy}:")
    if uczniowie:
        for uczen in uczniowie:
            print(f" - {uczen}")
    else:
        print("Brak uczniów w tej klasie.")

    print(f"\nWychowawca klasy {nazwa_klasy}:")
    if wychowawcy:
        for wych in wychowawcy:
            print(f" - {wych}")
    else:
        print("Brak przypisanego wychowawcy.")


def wyswietl_ucznia(imie, nazwisko):
    znalezieni_uczniowie = [ucz for ucz in lista["uczniowie"] if ucz.imie == imie and ucz.nazwisko == nazwisko]

    if not znalezieni_uczniowie:
        print("Nie znaleziono ucznia.")
        return

    uczen = znalezieni_uczniowie[0]
    klasa_ucznia = uczen.klasa
    lekcje_klasy = set()

    print(f"\nUczeń: {uczen}\nKlasa: {klasa_ucznia}")
    print("\nLekcje i nauczyciele:")

    for nauczyciel in lista["nauczyciele"]:
        if klasa_ucznia in nauczyciel.klasy:
            lekcje_klasy.add((nauczyciel.przedmiot, f"{nauczyciel.imie} {nauczyciel.nazwisko}"))

    if lekcje_klasy:
        for lekcja, nauczyciel in sorted(lekcje_klasy):
            print(f" - {lekcja}: {nauczyciel}")
    else:
        print("Brak lekcji dla tej klasy.")


def wyszukaj_klasy_nauczyciela(imie, nazwisko):
    for nauczyciel in lista["nauczyciele"]:
        if nauczyciel.imie.lower() == imie.lower() and nauczyciel.nazwisko.lower() == nazwisko.lower():
            return nauczyciel.klasy
    return None

def wyszukaj_uczniow_wychowawcy(imie, nazwisko):
    for wychowawca in lista["wychowawcy"]:
        if wychowawca.imie.lower() == imie.lower() and wychowawca.nazwisko.lower() == nazwisko.lower():
            klasy_wychowawcy = wychowawca.klasy
            uczniowie = [uczen for uczen in lista["uczniowie"] if uczen.klasa in klasy_wychowawcy]
            return uczniowie
    return None

print("Witaj w systemie bazy szkolnej")

while True:

    print("Wybierz jedną z poniższych opcji (wybierając 1-3)")
    komenda = input("""
    1. Utwórz
    2. Zarządzaj
    3. Koniec
    \n""").strip().casefold()

    match komenda:
        case "1":
            print("Wybierz jedną z poniższych opcji (wybierając 1-4)")
            utworz = input("""
            1. Uczeń
            2. Nauczyciel
            3. Wychowawca
            4. Koniec
            \n""").strip().casefold()

            if utworz.strip().casefold() in ("1", "Uczeń","Uczen", "uczen", "uczeń"):
                imie = input("Podaj imię ucznia:\n")
                nazwisko = input("Podaj nazwisko ucznia:\n")
                klasa = input("Do której klasy należy:\n")
                dodaj_ucznia(imie, nazwisko, klasa)

            elif utworz.strip().casefold() in ("2", "nauczyciel"):
                imie = input("Podaj imię:\n")
                nazwisko = input("Podaj nazwisko:\n")
                klasy_input = input("Podaj klasy, w których uczy (oddziel przecinkami):\n")
                klasy = [k.strip() for k in klasy_input.split(",") if k.strip()]
                przedmiot = input("Czego uczy (np. matematyka, biologia):\n")
                stanowisko = "Nauczyciel"
                dodaj_nauczyciela(imie, nazwisko, klasy, przedmiot)

            elif utworz.strip().casefold() in ("3", "Wychowawca", "wychowawca"):
                imie = input("Podaj imię:\n")
                nazwisko = input("Podaj nazwisko:\n")
                klasy_input = input("Podaj klasy, w których jest wychowawcą (oddziel przecinkami):\n")
                klasy = [k.strip() for k in klasy_input.split(",")]
                przedmiot = input("Czego uczy (matematyka, biologia):\n")
                stanowisko = "Wychowawca"
                dodaj_wychowawce(imie, nazwisko, klasy, przedmiot)

            elif utworz in ("4", "koniec"):
                pass

        case "2":
            print("Wybierz jedną z poniższych opcji (wybierając 1-5)")
            zarzadzaj = input("""
                   1. Klasa
                   2. Uczeń
                   3. Nauczyciel
                   4. Wychowawca
                   5. Koniec
                   \n""").strip().casefold()

            match zarzadzaj:
                case "1":
                    nazwa_klasy = input("Podaj nazwę klasy (np. 1A):\n").strip()
                    wyswietl_klase(nazwa_klasy)
                case "2":
                    imie = input("Podaj imię ucznia:\n").strip()
                    nazwisko = input("Podaj nazwisko ucznia:\n").strip()
                    wyswietl_ucznia(imie, nazwisko)

                case "3":
                    imie = input("Podaj imię nauczyciela:\n")
                    nazwisko = input("Podaj nazwisko nauczyciela:\n")
                    klasy = wyszukaj_klasy_nauczyciela(imie, nazwisko)
                    if klasy:
                        print(f"Nauczyciel {imie} {nazwisko} prowadzi klasy: {', '.join(klasy)}")
                    else:
                        print("Nie znaleziono nauczyciela o podanym imieniu i nazwisku.")

                case "4":
                    imie = input("Podaj imię wychowawcy:\n")
                    nazwisko = input("Podaj nazwisko wychowawcy:\n")
                    uczniowie = wyszukaj_uczniow_wychowawcy(imie, nazwisko)
                    if uczniowie is not None:
                        if uczniowie:
                            print(f"Wychowawca {imie} {nazwisko} prowadzi następujących uczniów:")
                            for uczen in uczniowie:
                                print(f"- {uczen.imie} {uczen.nazwisko} ({uczen.klasa})")
                        else:
                            print("Wychowawca nie ma przypisanych uczniów.")
                    else:
                        print("Nie znaleziono wychowawcy o podanym imieniu i nazwisku.")

                case "5":
                    print("Powrót do głównego menu.")
                    continue

        case "3":
            for kategoria, obiekty in lista.items():
                print(f"\n{kategoria.upper()}:")
                for obiekt in obiekty:
                    print(f" - {obiekt}")
            print("Zakończono działanie programu.")
            break


