class Pies:
    def __init__(self, imie):
        self.imie = imie

    def szczekaj(self):
        print(f"{self.imie} szczeka: Hau hau!")

    def __str__(self):
        return f"Pies {self.imie}"