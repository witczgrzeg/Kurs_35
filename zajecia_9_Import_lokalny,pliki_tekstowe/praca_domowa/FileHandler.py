import json

class FileHandler:
    def __init__(self, produkty_file, historia_file, saldo_file):
        self.produkty_file = produkty_file
        self.historia_file = historia_file
        self.saldo_file = saldo_file
        self.produkty = self.load_produkty_file()
        self.historia = self.load_historia_file()
        self.saldo = self.load_saldo_file()

    def load_produkty_file(self):
        with open(self.produkty_file) as file:
            produkty = json.load(file)
            return produkty

    def load_historia_file(self):
        with open(self.historia_file) as file:
            historia = json.load(file)
            return historia

    def load_saldo_file(self):
        with open(self.saldo_file) as file:
            saldo = file.read().strip()
            if saldo:
                return float(saldo)
            else:
                return 0.0

    def save_produkty_file(self):
        with open(self.produkty_file, "w") as file:
            file.write(json.dumps(self.produkty, indent=4))

    def save_historia_file(self):
        with open(self.historia_file, "w") as file:
            file.write(json.dumps(self.historia, indent=4))

    def save_saldo_file(self):
        with open(self.saldo_file, "w") as file:
            file.write(str(self.saldo))

file_handler = FileHandler("produkty.json", "historia.json", "saldo.txt")