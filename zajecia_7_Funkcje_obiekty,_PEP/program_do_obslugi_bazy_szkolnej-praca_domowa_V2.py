class Nauczyciel:
    def __init__(self, imie, nazwisko, klasy, przedmiot):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasy = klasy
        self.przedmiot = przedmiot
        self.stanowisko = "Nauczyciel"

    def __repr__(self):
        klasy_str = ", ".join(self.klasy)
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
        klasy_str = ", ".join(self.klasy)
        return f"{self.imie} {self.nazwisko}, {klasy_str}, {self.przedmiot}, {self.stanowisko}"

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
        Nauczyciel("Tomasz", "Wrona", ["1A"], "Fizyka", "Nauczyciel"),
        Nauczyciel("Monika", "Zielińska", ["1B"], "Chemia", "Nauczyciel"),
        Nauczyciel("Karolina", "Wiśniewska", ["1C"], "Język angielski", "Nauczyciel"),
        Nauczyciel("Marek", "Nowicki", ["1A"], "Wychowanie fizyczne", "Nauczyciel")
    ],
    "wychowawcy":[
        Wychowawca("Alicja", "Kaczmarek", ["0"], "Historia", "Dyrektor"),
        Wychowawca("Agnieszka", "Piotrowska", ["1A"], "Matematyka", "Wychowawca"),
        Wychowawca("Rafał", "Sadowski", ["1B"], "Polski", "Wychowawca"),
        Wychowawca("Beata", "Jankowska", ["1C"], "Biologia", "Wychowawca"),
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

# # Jeśli chcesz ładnie wydrukować:
# for kategoria, obiekty in lista.items():
#     print(f"\n{kategoria.upper()}:")
#     for obiekt in obiekty:
#         print(f" - {obiekt}")

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

            if utworz in ("1", "Uczeń", "Uczen"):
                imie = input("Podaj imię ucznia:\n")
                nazwisko = input("Podaj nazwisko ucznia:\n")
                klasa = input("Do której klasy należy:\n")
                nowy_uczen = Uczen(imie, nazwisko, klasa)
                lista["uczniowie"].append(nowy_uczen)


            elif utworz.strip().lower() in ("2", "Nauczyciel"):
                imie = input("Podaj imię:\n")
                nazwisko = input("Podaj nazwisko:\n")
                klasy_input = input("Podaj klasy, w których uczy (oddziel przecinkami):\n")
                klasy = [k.strip() for k in klasy_input.split(",") if k.strip()]  # lista klas, usunięcie pustych
                przedmiot = input("Czego uczy (np. matematyka, biologia):\n")
                stanowisko = "Nauczyciel"
                nowy_nauczyciel = Nauczyciel(imie, nazwisko, klasy, przedmiot, stanowisko)
                lista["Nauczyciele"].append(nowy_nauczyciel)

            elif utworz.strip().lower() in ("3", "Wychowawca"):
                imie = input("Podaj imię:\n")
                nazwisko = input("Podaj nazwisko:\n")
                klasy_input = input("Podaj klasy, w których jest wychowawcą (oddziel przecinkami):\n")
                klasy = [k.strip() for k in klasy_input.split(",")]  # tworzymy listę klas
                przedmiot = input("Czego uczy (matematyka, biologia):\n")
                stanowisko = "Wychowawca"
                nowy_wychowawca = Wychowawca(imie, nazwisko, klasy, przedmiot, stanowisko)
                lista["wychowawcy"].append(nowy_wychowawca)

            elif utworz in ("4", "koniec"):
                break

        case "2":
            print("Wybierz jedną z poniższych opcji (wybierając 1-5)")
            zarzadzaj = input("""
                   1. Klasa
                   2. Uczeń
                   3. Nauczyciel
                   4. Wychowawca
                   5. Koniec
                   \n""").strip().casefold()

            if zarzadzaj in ("1", "klasa"):
                pass
            elif zarzadzaj.strip().lower() in ("5", "koniec"):
                break
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
            for kategoria, obiekty in lista.items():
                print(f"\n{kategoria.upper()}:")
                for obiekt in obiekty:
                    print(f" - {obiekt}")
            print("Zakończono działanie programu.")
            break