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


uzytkownicy = [
    {}
]


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
        case "2":
            print("Wybierz jedną z poniższych opcji (wybierając 1-5)")
            zarzadzaj = input("""
                       1. Klasa
                       2. Uczeń
                       3. Nauczyciel
                       4. Wyhowawca
                       5. Koniec 
                       """)
        case "3":
            print("Zakończono działanie programu.")
            break