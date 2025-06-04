def przywitaj_sie(imie, nazwisko):
    print(f"Witaj {imie} {nazwisko}!")
    return f"Witaj {imie} {nazwisko}!"

przywitaj_sie("Grzegorz", "Witczak")

def przywitaj_sie_z_args(*moje_args):
    argumenty = moje_args
    pierwszy_argument = moje_args[0]
    print(argumenty)

przywitaj_sie_z_args(1, 2, 3, "Grzegorz", "Witczak")

def przywitaj_sie_z_kwargs(**moje_kwargs):
    print(moje_kwargs)

przywitaj_sie_z_kwargs(imie="Grzegorz", nazwisko="Witczak", wiek= 37, miasto= "Łódź")

def przywitaj_sie_z_args_kwargs(imie, nazwisko, *moje_args, **moje_kwargs):
    print(imie)
    print(nazwisko)
    print(moje_args)
    print(moje_kwargs)
