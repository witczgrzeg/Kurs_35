class Chomik:
    def __init__(self, imie: str, wiek: int):
        self.imie = imie
        self.wiek = wiek

    def __str__(self):
        return f"Chomik {self.imie}, wiek {self.wiek} lat"