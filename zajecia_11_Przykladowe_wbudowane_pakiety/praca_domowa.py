"""
Napisz program, który odczyta wejściowy plik CSV, następnie zmodyfikuje go i wyświetli w terminalu jego zawartość, a na końcu zapisze w wybranej lokalizacji.

Uruchomienie programu przez terminal:
python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>

 <plik_wejsciowy> - nazwa pliku, który ma zostać odczytany, np. in.csv
 <plik_wyjsciowy> - nazwa pliku, do którego ma zostać zapisana zawartość, np. out.csv
<zmiana_x> - Zmiana w postaci "x,y,wartosc" - x (kolumna) oraz y (wiersz) są współrzędnymi liczonymi od 0, natomiast "wartosc" zmianą która ma trafić na podane miejsce.

Przykładowy plik wejściowy znajduje się w repozytorium pod nazwą "in.csv".

Przykład działania:
python reader.py in.csv out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
Z pliku in.csv:
drzwi,3,7,0
kanapka,12,5,1
pedzel,22,34,5
plakat,czerwony,8,kij
Ma wyjść plik out.csv:
gitara,3,7,0
kanapka,12,5,kubek
pedzel,17,34,5
plakat,czerwony,8,0

"""