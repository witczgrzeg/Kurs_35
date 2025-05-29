"""
Jesteś szefem firmy technologicznej tworzącej system zarządzania dla międzynarodowego lotniska. System ten ma obsługiwać dane związane z lotami, liniami lotniczymi, pasażerami oraz stewardessami. Każdy lot może mieć przypisanych wielu pasażerów i jedną stewardessę, natomiast linie lotnicze mogą obsługiwać nieograniczoną liczbę lotów. Celem jest stworzenie programu, który pozwoli na efektywne zarządzanie i dostarczanie właściwych informacji na potrzeby logistyki i obsługi klienta lotniska.

**Program do zarządzania danymi lotów na międzynarodowym lotnisku**
Program powinien umożliwić:
1. Dodanie nowych danych do systemu:
   - Pasażera z przypisanym numerem lotu.
   - Stewardessy z przypisanym numerem lotu.
   - Linii lotniczej, która może obsługiwać wiele różnych lotów.
2. Przeglądanie i zarządzanie istniejącymi informacjami:
   - Pobranie listy pasażerów danego lotu.
   - Znalezienie przypisanej linii lotniczej dla wybranego pasażera.
   - Wyświetlenie listy lotów danej linii lotniczej.
   - Otrzymanie listy wszystkich pasażerów dla lotu, którego stewardessą jest wybrana osoba.
**Polecenia programu**
Po uruchomieniu, program powinien wyświetlić menu z następującymi komendami:
- dodaj - przechodzi do menu dodawania nowych danych.
- przeglądaj - przechodzi do menu przeglądania i zarządzania danymi.
- zakończ - kończy działanie programu.
**Menu dodawania danych (dodaj):**
Użytkownik może wybrać:
- pasażer - dodanie pasażera wymaga wprowadzenia imienia i nazwiska, numeru lotu.
- stewardessa - dodanie stewardessy wymaga wprowadzenia imienia i nazwiska, numeru lotu, do którego jest przypisana.
- linia_lotnicza - dodanie linii lotniczej wymaga wprowadzenia jej nazwy.
- zakończ_dodawanie - powrót do głównego menu.
**Menu przeglądania i zarządzania danymi (przeglądaj):**
Użytkownik może wybrać:
- lot - wprowadzenie numeru lotu wyświetla listę pasażerów tego lotu.
- pasażer - wprowadzenie imienia i nazwiska pasażera wyświetla nazwę linii lotniczej.
- linia_lotnicza - wprowadzenie nazwy linii lotniczej wyświetla listę lotów obsługiwanych przez linię.
- stewardessa - wprowadzenie imienia i nazwiska stewardessy wyświetla listę pasażerów jej lotu.
- zakończ_przeglądanie - powrót do głównego menu.
**Zakończenie pracy programu**
Polecenie zakończ powoduje zamknięcie aplikacji.
"""


class Pasazer:
    def __init__(self, imie, nazwisko, numer_lotu, numer_miejsca_w_samolocie=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_lotu = numer_lotu
        self.numer_miejsca_w_samolocie = numer_miejsca_w_samolocie

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} ({self.numer_lotu}, {self.numer_miejsca_w_samolocie})"


class LiniaLotnicza:
    def __init__(self, nazwa, lista_lotow):
        self.nazwa = nazwa
        self.loty = lista_lotow

    def dodaj_lot(self, lot):
        self.loty.append(lot)

    def __repr__(self):
        return f"{self.nazwa} ({len(self.loty)} lotów) - numery lotow {self.loty}"


class Stewardessa:
    def __init__(self, imie, nazwisko, numer_lotu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_lotu = numer_lotu

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} ({self.numer_lotu})"


lotnisko = {
    "pasazerowie": [
        Pasazer("Jan", "Kowalski", "LO123", "12A"),
        Pasazer("Anna", "Nowak", "LO123", "12B"),
        Pasazer("Piotr", "Zalewski", "LO456", "14C"),
    ],
    "linie_lotnicze": [
        LiniaLotnicza("LOT", ["LO123", "LO456"]),
        LiniaLotnicza("Ryanair", ["RY123", "RY456"]),
    ],
    "stewardessy": [
        Stewardessa("Anna", "Nowak", "LO123"),
        Stewardessa("Maria", "Kowalska", "LO456"),
    ],
}


def wyszukaj_pasazerow_dla_lotu(numer_lotu):
    pasazerowie_dla_lotu = []
    for pasazer in lotnisko.get("pasazerowie"):
        if pasazer.numer_lotu == numer_lotu:
            pasazerowie_dla_lotu.append(pasazer)
    return pasazerowie_dla_lotu


def wyszukaj_linie_lotnicza_pasazera(imie, nazwisko):
    numer_lotu_pasazera = None
    for pasazer in lotnisko.get("pasazerowie"):
        if pasazer.imie == imie and pasazer.nazwisko == nazwisko:
            numer_lotu_pasazera = pasazer.numer_lotu
            break
    if numer_lotu_pasazera:
        for linia in lotnisko.get("linie_lotnicze"):
            if numer_lotu_pasazera in linia.loty:
                return linia.nazwa


def wyszukaj_loty_linii_lotniczej(nazwa_linii):
    for linia in lotnisko.get("linie_lotnicze"):
        if linia.nazwa == nazwa_linii:
            return linia.loty


def wyszukaj_lot_stewardessy(imie, nazwisko):
    for stewardessa in lotnisko.get("stewardessy"):
        if stewardessa.imie == imie and stewardessa.nazwisko == nazwisko:
            return stewardessa.numer_lotu


while True:
    wybor_uzytkownika = input("Wybierz opcję:\n1. Dodaj\n2. Przeglądaj\n3. Zakończ\n")

    match wybor_uzytkownika:
        case "1":
            obiekt_do_dodania = input(
                "Co chcesz dodać?:\n1. Pasażera\n2. Stewardessę\n3. Linię lotniczą\n"
            )
            if obiekt_do_dodania.strip() in (
                "1",
                "Pasażer",
                "Pasażera",
                "pasażer",
                "pasażera",
            ):
                imie = input("Podaj imię pasażera: ")
                nazwisko = input("Podaj nazwisko pasażera: ")
                numer_lotu = input("Podaj numer lotu: ")
                numer_miejsca = input("Podaj numer miejsca w samolocie: ")
                nowy_pasazer = Pasazer(imie, nazwisko, numer_lotu, numer_miejsca)
                lotnisko["pasazerowie"].append(nowy_pasazer)
            elif obiekt_do_dodania.strip() in (
                "2",
                "Stewardessa",
                "Stewardessę",
                "stewardessa",
                "stewardessę",
            ):
                imie = input("Podaj imię stewardessy: ")
                nazwisko = input("Podaj nazwisko stewardessy: ")
                numer_lotu = input("Podaj numer lotu: ")
                nowa_stewardessa = Stewardessa(imie, nazwisko, numer_lotu)
                lotnisko["stewardessy"].append(nowa_stewardessa)
            elif obiekt_do_dodania.strip() in ("3", "Linia lotnicza", "linia lotnicza"):
                nazwa = input("Podaj nazwę linii lotniczej: ")
                lista_lotow_linii = []
                while True:
                    numer_lotu = input("Podaj numer lotu: ")
                    if numer_lotu:
                        lista_lotow_linii.append(numer_lotu)
                    else:
                        break
                nowa_linia_lotnicza = LiniaLotnicza(nazwa, lista_lotow_linii)
                lotnisko["linie_lotnicze"].append(nowa_linia_lotnicza)
        case "2":
            opcja_do_przegladania = input(
                "Co chcesz przeglądać?:\n"
                "1. Lot\n"
                "2. Pasażer\n"
                "3. Linia lotnicza\n"
                "4. Stewardessa\n"
            )
            match opcja_do_przegladania:
                case "1":
                    numer_lotu = input("Podaj numer lotu: ")
                    pasazerowie_lotu = wyszukaj_pasazerow_dla_lotu(numer_lotu)
                    print(pasazerowie_lotu)
                case "2":
                    imie_pasazera = input("Podaj imię pasażera: ")
                    nazwisko_pasazera = input("Podaj nazwisko pasażera: ")
                    linia_pasazera = wyszukaj_linie_lotnicza_pasazera(
                        imie_pasazera, nazwisko_pasazera
                    )
                    print(linia_pasazera)
                case "3":
                    nazwa_linii = input("Podaj nazwę linii lotniczej: ")
                    loty_linii = wyszukaj_loty_linii_lotniczej(nazwa_linii)
                    print(loty_linii)
                case "4":
                    imie_stewardessy = input("Podaj imię stewardessy: ")
                    nazwisko_stewardessy = input("Podaj nazwisko stewardessy: ")
                    numer_lotu_stewardessy = wyszukaj_lot_stewardessy(
                        imie_stewardessy, nazwisko_stewardessy
                    )
                    pasazerowie_lotu = wyszukaj_pasazerow_dla_lotu(
                        numer_lotu_stewardessy
                    )
                    print(pasazerowie_lotu)
        case "3":
            break
