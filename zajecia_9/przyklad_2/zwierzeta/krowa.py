class Krowa:
    def __init__(self, imie):
        self.imie = imie
        self.glos = "Muuu"
        self.wiek = 0
        self.waga = 0

    def __str__(self):
        return f"Krowa {self.imie} ma {self.wiek} lat i waze {self.waga} kg"