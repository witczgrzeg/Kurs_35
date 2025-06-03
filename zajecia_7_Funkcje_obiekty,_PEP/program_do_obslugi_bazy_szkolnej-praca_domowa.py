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


lista_uzytkownikow = [
    {
        "stanowisko": "Dyrektor",
        "imie": "Alicja",
        "nazwisko": "Kaczmarek",
        "Klasa": "brak",
        "numer": "0"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Jan",
        "nazwisko": "Kowalski",
        "klasa": "Pierwsza",
        "numer": "1A"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Anna",
        "nazwisko": "Nowak",
        "klasa": "Pierwsza",
        "numer": "1A"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Tomasz",
        "nazwisko": "Wiśniewski",
        "klasa": "Pierwsza",
        "numer": "1A"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Kacper",
        "nazwisko": "Wójcik",
        "klasa": "Pierwsza",
        "numer": "1A"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Zofia",
        "nazwisko": "Kamińska",
        "klasa": "Pierwsza",
        "numer": "1A"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Mikołaj",
        "nazwisko": "Dąbrowski",
        "klasa": "Pierwsza",
        "numer": "1A"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Oliwia",
        "nazwisko": "Nowak",
        "klasa": "Pierwsza",
        "numer": "1A"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Tomasz",
        "nazwisko": "Lis",
        "klasa": "Pierwsza",
        "numer": "1A"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Natalia",
        "nazwisko": "Mazur",
        "klasa": "Pierwsza",
        "numer": "1B"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Wiktor",
        "nazwisko": "Grabowski",
        "klasa": "Pierwsza",
        "numer": "1B"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Julia",
        "nazwisko": "Pawlak",
        "klasa": "Pierwsza",
        "numer": "1B"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Mateusz",
        "nazwisko": "Michalak",
        "klasa": "Pierwsza",
        "numer": "1B"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Emilia",
        "nazwisko": "Baran",
        "klasa": "Pierwsza",
        "numer": "1B"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Antoni",
        "nazwisko": "Witkowski",
        "klasa": "Pierwsza",
        "numer": "1B"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Aleksandra",
        "nazwisko": "Kaczmarek",
        "klasa": "Pierwsza",
        "numer": "1B"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Bartłomiej",
        "nazwisko": "Czarnecki",
        "klasa": "Pierwsza",
        "numer": "1B"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Filip",
        "nazwisko": "Kowalczyk",
        "klasa": "Pierwsza",
        "numer": "1C"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Lena",
        "nazwisko": "Zawadzka",
        "klasa": "Pierwsza",
        "numer": "1C"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Michał",
        "nazwisko": "Nowicki",
        "klasa": "Pierwsza",
        "numer": "1C"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Martyna",
        "nazwisko": "Szymańska",
        "klasa": "Pierwsza",
        "numer": "1C"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Jakub",
        "nazwisko": "Woźniak",
        "klasa": "Pierwsza",
        "numer": "1C"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Zuzanna",
        "nazwisko": "Adamska",
        "klasa": "Pierwsza",
        "numer": "1C"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Szymon",
        "nazwisko": "Rutkowski",
        "klasa": "Pierwsza",
        "numer": "1C"
    },
    {
        "stanowisko": "Uczen",
        "imie": "Julia",
        "nazwisko": "Krawczyk",
        "klasa": "Pierwsza",
        "numer": "1C"
    },
    {
        "stanowisko": "Wychowarca",
        "imie": "Agnieszka",
        "nazwisko": "Piotrowska",
        "klasa": "Pierwsza",
        "numer": "1A"
    },
    {
        "stanowisko": "Wychowarca",
        "imie": "Rafał",
        "nazwisko": "Sadowski",
        "klasa": "Pierwsza",
        "numer": "1B"
    },
    {
        "stanowisko": "Wychowarca",
        "imie": "Beata",
        "nazwisko": "Jankowska",
        "klasa": "Pierwsza",
        "numer": "1C"
    }
]

def dodaj_uzytkownika(stanowisko, imie, nazwisko, klasa, numer):
    uzytkownik = {
        "stanowisko": stanowisko,
        "imie": imie,
        "nazwisko": nazwisko,
        "klasa": klasa,
        "numer": numer
    }
    lista_uzytkownikow.append(uzytkownik)

    print(f"dodano: stanowisko:{stanowisko}, imię {imie} {nazwisko}, do {klasa} {numer}")

dodaj_uzytkownika("uczen", "XjanuszX", "XkowalX", "Trzecia", "3B")
dodaj_uzytkownika("nauczyciel", "Jan", "Kowalski","Pierwsza", "1A")
for uzytkownik in lista_uzytkownikow:
    print(uzytkownik)

print("Witaj w systemie bazy szkolnej")

while True:

    print("Wybierz jedną z poniższych opcji (wybierając 1-3)")
    komenda = input("""
    1. Utwórz
    2. Zarządzaj
    3. Koniec
    \n""")
    komenda = komenda.lower()

    match komenda:
        case "1":
            print("Wybierz jedną z poniższych opcji (wybierając 1-4)")
            utworz = input("""
            1. Uczeń
            2. Nauczyciel
            3. Wychowawca
            4. Koniec 
            """)
            match utworz:
                case "1":
                   print ("wpisz coś")

        case "2":
            print("Wybierz jedną z poniższych opcji (wybierając 1-5)")
            zarzadzaj = input("""
                       1. Klasa
                       2. Uczeń
                       3. Nauczyciel
                       4. Wyhowawca
                       5. Koniec 
                       """)
            match zarzadzaj:
                case "1":
                    for klasa in lista_uzytkownikow:
                        if klasa["klasa"] == uzytkownik:
                            print(klasa)

        case "3":
            print("Zakończono działanie programu.")
            break