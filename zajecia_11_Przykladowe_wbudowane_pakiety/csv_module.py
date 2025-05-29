import csv
import os

os.chdir('/home/michal/Documents')
print("lista_uczniow.csv" in os.listdir())
with open("lista_uczniow.csv") as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)

with open("lista_uczniow2.csv", mode="a+") as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Jan", "Kowalski", "5"])