import json


class FileHandler:
    def __init__(self, ksiegozbior_file, saldo_file, historia_file):
        self.ksiegozbior_file = ksiegozbior_file
        self.saldo_file = saldo_file
        self.historia_file = historia_file
        self.ksiegozbior = self.load_ksiegozbior_file()
        self.historia = self.load_history_file()
        self.saldo = self.load_saldo_file()

    def load_ksiegozbior_file(self):
        with open(self.ksiegozbior_file) as file:
            ksiegozbior = json.load(file)
            return ksiegozbior

    def load_history_file(self):
        with open(self.historia_file) as file:
            historia = json.load(file)
            # return historia
        return historia

    def load_saldo_file(self):
        with open(self.saldo_file) as file:
            saldo = file.read().strip()
            return float(saldo)

    def save_ksiegozbior_file(self):
        with open(self.ksiegozbior_file, "w") as file:
            file.write(json.dumps(self.ksiegozbior, indent=4))

    def save_historia_file(self):
        with open(self.historia_file, "w") as file:
            file.write(json.dumps(self.historia, indent=4))

    def save_saldo_file(self):
        with open(self.saldo_file, "w") as file:
            file.write(str(self.saldo))


file_handler = FileHandler("ksiegozbior.json", "saldo.txt", "historia.json")


def save_temporary_data(file_handler, lista_ksiazek, saldo, historia):
    file_handler.ksiegozbior = lista_ksiazek
    file_handler.saldo = saldo
    file_handler.historia = historia
    file_handler.save_ksiegozbior_file()
    file_handler.save_saldo_file()
    file_handler.save_historia_file()
