ksiazki = [
    {
        "tytul": "Harry Potter",
        "autor": "J.K. Rowling",
        "rok_wydania": 1997,
        "gatunek": "fantasy",
    },
    {
        "tytul": "Władca Pierścieni",
        "autor": "J.R.R. Tolkien",
        "rok_wydania": 1954,
        "gatunek": "fantasy",
    },
]


def dodaj_ksiazke(tytul, autor, rok_wydania, gatunek):
    ksiazka = {
        "tytul": tytul,
        "autor": autor,
        "rok_wydania": rok_wydania,
        "gatunek": gatunek,
    }
    ksiazki.append(ksiazka)
    print(f"Dodano książkę: {tytul} autorstwa {autor}.")


ksiazki.append(
    {
        "tytuł": "Wiedźmin",
        "autor": "Andrzej Sapkowski",
        "rok_wydania": 1990,
        "gatunek": "fantasy",
    }
)


def wyszukaj_ksiazke(tytul):
    for ksiazka in ksiazki:
        if ksiazka["tytul"] == tytul:
            return ksiazka


dodaj_ksiazke("Złodziejka książek", "Markus Zusak", 2005, "powieść")
print(ksiazki)


class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania, gatunek):
        self.nazwa = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek

    def __str__(self):
        return f"{self.nazwa} ({self.rok_wydania}) - {self.autor} [{self.gatunek}]"


ksiazka = Ksiazka("Wiedźmin", "Andrzej Sapkowski", 1990, "fantasy")
print(ksiazka)

print(ksiazka.nazwa)
print(ksiazka.rok_wydania)
ksiazka.autor = "Michał Ziętkowski"
print(ksiazka)

ksiazka_2 = Ksiazka("Harry Potter i Więzień Askabanu", "J.K. Rowling", 1997, "fantasy")


lista_kisazek = [
    ksiazka,
    ksiazka_2,
    Ksiazka("Władca Pierścieni", "J.R.R. Tolkien", 1954, "fantasy"),
    Ksiazka("Złodziejka książek", "Markus Zusak", 2005, "powieść"),
]


auto = {
    "marka": "Audi",
    "model": "A4",
    "rok_produkcji": 2020,
    "kolor": "czarny",
    "przebieg": 15000,
    "aktualny_bieg": "neutralny",
    "silnik_wlaczony": False,
    "predkosc": 0,
    "rodzaj_opon": "letnie",
}


def wlacz_silnik(auto):
    if auto["silnik_wlaczony"]:
        print("Silnik już jest włączony.")
    else:
        auto["silnik_wlaczony"] = True
        print("Silnik został włączony.")


class Auto:
    def __init__(
        self,
        marka,
        model,
        rok_produkcji,
        kolor,
        przebieg,
        aktualny_bieg,
        silnik_wlaczony,
        predkosc,
        rodzaj_opon,
    ):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.kolor = kolor
        self.przebieg = przebieg
        self.aktualny_bieg = aktualny_bieg
        self.silnik_wlaczony = silnik_wlaczony
        self.predkosc = predkosc
        self.rodzaj_opon = rodzaj_opon

    def zmien_opony(self, nowy_rodzaj_opon):
        self.rodzaj_opon = nowy_rodzaj_opon
        print(f"Zmieniono opony na {nowy_rodzaj_opon}.")

    def wlacz_silnik(self):
        if self.silnik_wlaczony:
            print("Silnik już jest włączony.")
        else:
            self.silnik_wlaczony = True
            print("Silnik został włączony.")


auto = Auto("Audi", "A4", 2020, "czarny", 15000, "neutralny", False, 0, "letnie")

auto.wlacz_silnik()
print(auto.silnik_wlaczony)
if auto.silnik_wlaczony:
    print("Silnik jest włączony.")
else:
    print("Silnik jest wyłączony.")


class Ksiazki:
    def __init__(self, ksiazki):
        self.ksiazki = ksiazki
