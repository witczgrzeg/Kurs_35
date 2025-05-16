ilosc_towaru = int(input("Podaj ilość towaru: "))


ilosc_paczek = 1
paczka_z_najwieksza_pusta_waga = 20
numer_paczki_z_najwieksza_pusta_waga = None
waga_paczki = 0
for element in range(ilosc_towaru):
    waga_towaru = float(input(f"Podaj wagę towaru {element + 1}: "))
    if waga_towaru + waga_paczki > 20:
        print("Przekroczono maksymalną wagę paczki. Tworzymy nową paczkę")
        if 20 - waga_paczki > 20 - paczka_z_najwieksza_pusta_waga:
            paczka_z_najwieksza_pusta_waga = waga_paczki
            numer_paczki_z_najwieksza_pusta_waga = ilosc_paczek
        waga_paczki = waga_towaru
        ilosc_paczek += 1
    else:
        waga_paczki += waga_towaru
