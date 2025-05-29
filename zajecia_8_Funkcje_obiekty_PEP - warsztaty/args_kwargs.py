def przywitaj_sie(imie, nazwisko):
    print(f"Witaj {imie} {nazwisko}!")
    return f"Witaj {imie} {nazwisko}!"


przywitaj_sie("Michał", "Ziętkowski")


def przywitaj_sie_z_args(*moje_args):
    argumenty = moje_args
    pierwszy_argument = moje_args[0]
    print(argumenty)


przywitaj_sie_z_args(1, 2, 3, "Michał", "Ziętkowski")


def przywitaj_sie_z_kwargs(**moje_kwargs):
    print(moje_kwargs)


przywitaj_sie_z_kwargs(imie="Michał", nazwisko="Ziętkowski", wiek=30, miasto="Szczecin")


def przywitaj_sie_z_args_kwargs(imie, nazwisko, *moje_args, **moje_kwargs):
    print(imie)
    print(nazwisko)
    print(moje_args)
    print(moje_kwargs)


przywitaj_sie_z_args_kwargs(
    "Jan",
    "Kowalski",
    1,
    2,
    3,
    imie="Michał",
    nazwisko="Ziętkowski",
    wiek=30,
    miasto="Szczecin",
)
