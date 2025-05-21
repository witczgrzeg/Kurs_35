plec_input = input("Podaj płeć: ").lower()

if plec_input == "mezczyzna" or plec_input == "kobieta":
    uzytkownik = {"plec": plec_input}
    print("Zapisano płeć:", uzytkownik["plec"])
else:
    print("Niepoprawna wartość!")

print(plec_input)