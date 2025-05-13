'''
Quiz wiedzy o podstawach Pythona

Wczytaj odpowiedzi użytkownika na 10 pytań:
1. Typ liczby 5?
2. Typ wartości 'Hello'?
3. Czy zmienne mają określony typ przy deklaracji? (tak/nie)
4. Typ wyniku 5/2?
5. Typ wyniku 2+3?
6. Jak zapisać tekst z apostrofem ("I'm")? ('...' lub "...")
7. Które wyrażenie daje True? (5>2)
8. Co oznacza operator %? (reszta/dzielenie/mnożenie)
9. Czy można zmieniać typ zmiennej? (tak/nie)
10. Wynik True and False to True? (tak/nie)

Policz punkty za poprawne odpowiedzi.
Jeśli >=7 punktów - "Quiz zaliczony", w przeciwnym razie "Quiz niezaliczony".
'''

punktacja_uzytkownika = 0

# Pytanie 1
odpowiedz = input("1. Typ liczby 5? (int/float): ")
punktacja_uzytkownika += 1 * (odpowiedz.lower() == "int")

# Pytanie 2
odpowiedz = input("2. Typ wartości 'Hello'? (str/int): ")
punktacja_uzytkownika += 1 * (odpowiedz == "str")

# Pytanie 3
odpowiedz = input("3. Czy zmienne mają określony typ przy deklaracji? (tak/nie): ")
punktacja_uzytkownika += 1 * (odpowiedz == "nie")

# Pytanie 4
odpowiedz = input("4. Typ wyniku 5/2? (int/float): ")
punktacja_uzytkownika += 1 * (odpowiedz.lower() == "float")

# Pytanie 5
odpowiedz = input("5. Typ wyniku 2+3? (int/float): ")
punktacja_uzytkownika += 1 * (odpowiedz.lower() == "int")

# Pytanie 6
odpowiedz = input("6. Jak zapisać tekst z apostrofem ('I'm')? podwojne apostrofy czy pojedyncze?: ")
punktacja_uzytkownika += 1 * (odpowiedz.lower() == "podwojne")

# Pytanie 7
odpowiedz = input("7. Które wyrażenie daje True? (5>2/2>5): ")
punktacja_uzytkownika += 1 * (odpowiedz == "5>2")

# Pytanie 8
odpowiedz = input("8. Co oznacza operator %? (reszta/dzielenie/mnożenie): ")
punktacja_uzytkownika += 1 * (odpowiedz.upper() == "RESZTA")

# Pytanie 9
odpowiedz = input("9. Czy można zmieniać typ zmiennej? (tak/nie): ")
punktacja_uzytkownika += 1 * (odpowiedz == "tak")

# Pytanie 10
odpowiedz = input("10. Wynik True and False to True? (tak/nie): ")
punktacja_uzytkownika += 1 * (odpowiedz == "nie")

print(f"Twoja punktacja to: {punktacja_uzytkownika}/10")

print("Quiz zaliczony!" * (punktacja_uzytkownika >= 7) + "Quiz niezaliczony!" * (punktacja_uzytkownika < 7))