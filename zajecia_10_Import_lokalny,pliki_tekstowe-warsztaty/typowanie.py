from typing import List, Union, Optional, TypedDict


class Osoba(TypedDict):
    imie: str
    nazwisko: str
    wiek: int
    plec: Optional[str] = None


osoba: Osoba = {"nazwisko": "Kowalski", "wiek": 30, "plec": "M"}

imie: str = "Jan"

imiona: List[str] = ["Jan", "Anna", "Piotr", 20]


def zwieksz_moj_wiek_o_wybrana_liczbe(moj_wiek: int, wybrana_liczba: int) -> int | None:
    x = moj_wiek / wybrana_liczba
    return moj_wiek + wybrana_liczba


# zwieksz_moj_wiek_o_wybrana_liczbe("osiemnascie", 2)
