"""
Treść zadania

Napisz program śledzący czas ćwiczeń na siłowni.

Działanie programu:

    Program pyta o planowany czas treningu (w minutach).

    Następnie w pętli pobiera kolejne czasy poszczególnych ćwiczeń (w minutach).

    Każde ćwiczenie musi mieć czas od 5 do 45 minut.

    Jeśli podany czas jest spoza zakresu, program kończy wprowadzanie.

    Suma czasów ćwiczeń nie może przekroczyć 150% planowanego czasu treningu - jeśli dodanie kolejnego ćwiczenia przekracza ten limit, program kończy wprowadzanie.

    Na koniec program wyświetla:

        Łączny czas ćwiczeń,

        Procent wykorzystania planu,

        Liczbę ćwiczeń trwających dłużej niż 15 minut,

        Najdłuższe pojedyncze ćwiczenie.

Przykłady

Przykład 1:

text
Plan: 60 minut
Czasy: 30, 35, 25 (przekroczenie limitu)

Podsumowanie:
Łączny czas ćwiczeń: 90 minut
Procent wykorzystania planu: 150.00%
Ćwiczenia >15 min: 3
Najdłuższe ćwiczenie: 35 minut

Przykład 2:

text
Plan: 45 minut
Czasy: 10, 15, 20

Podsumowanie:
Łączny czas ćwiczeń: 45 minut
Procent wykorzystania planu: 100.00%
Ćwiczenia >15 min: 1
Najdłuższe ćwiczenie: 20 minut

Przykład 3:

text
Plan: 30 minut
Czasy: 25, 50 (błąd)

Podsumowanie:
Łączny czas ćwiczeń: 25 minut
Procent wykorzystania planu: 83.33%
Ćwiczenia >15 min: 1
Najdłuższe ćwiczenie: 25 minut

"""
################ POSTARAJ SIE SAM ! #####################