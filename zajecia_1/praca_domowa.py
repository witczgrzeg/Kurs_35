"""
Program do generowania życzeń urodzinowych
Arrow down
Stwórz program, który generuje spersonalizowaną kartkę urodzinową. Program będzie prosił użytkownika o konkretne informacje, a następnie generował kartkę urodzinową na podstawie jego odpowiedzi. Wiek osoby powinien być obliczany na podstawie roku urodzenia podanego przez użytkownika.

1. Napisz program, który prosi użytkownika o podanie następujących informacji:

 - Imię odbiorcy
 - Rok urodzenia
 - Spersonalizowaną wiadomość
 - Imię nadawcy

2. Program powinien następnie obliczyć wiek odbiorcy na podstawie obecnego roku i roku urodzenia podanego przez użytkownika.

3. Wygeneruj spersonalizowaną kartkę urodzinową z następującą wiadomością:

[Imię odbiorcy], wszystkiego najlepszego z okazji [Wiek] urodzin!

[Spersonalizowana Wiadomość]

[Imię Nadawcy]

Wskazówki:

- Upewnij się, że program jest łatwy w obsłudze
- Podczas obliczania wieku odbiorcy, pamiętaj, aby konwertować dane wprowadzone przez użytkownika na odpowiedni typ zmiennej.
- Możesz zodyfikować szablon według własnego uznania. Upewnij się, że wyświetlasz wszystkie niezbędne zmienne.
"""

imie= input("Podaj imię odbiorcy: \n")
data_urodzenia= (int(input("Pdodaj datę urodzenia: \n")))
wiadomosc= input("Podaj spersonalizowaną wiadomość: \n")
imie2= input("Podaj swoje imię: \n")
urodziny= str(int(2025 - data_urodzenia))
print(imie+(" wszystkiego najpelszego z okazji "+(urodziny)+" urodzin!\n"+"\n"+wiadomosc+"\n"+"\n"+"Z poważaniem,\n"+imie2))