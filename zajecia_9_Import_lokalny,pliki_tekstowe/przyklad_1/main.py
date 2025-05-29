# import math_operations
from math_operations import dodawanie, odejmowanie, ciekawostka
import pies
import zajecia_9.przyklad_2.zwierzeta.pies as animals

def main():
    print("Hello, World!")

# print(math_operations.dodawanie(1, 2))
print(dodawanie(1, 2))
print(odejmowanie(2, 1))

pies = animals.Pies("Burek")
pies.szczekaj()

def ciekawostka():
    print("Ciekawostka: Pies to najlepszy przyjaciel człowieka!")

ciekawostka()