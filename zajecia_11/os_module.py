import os

print(os.getcwd())
print(os.listdir())
# os.chdir('..')
# print(os.getcwd())
# print(os.listdir())

nazwa_pliku = input("Podaj nazwę pliku: ")
if os.path.exists(nazwa_pliku):
    print("Plik istnieje")

print(os.path.join(os.getcwd(), nazwa_pliku))