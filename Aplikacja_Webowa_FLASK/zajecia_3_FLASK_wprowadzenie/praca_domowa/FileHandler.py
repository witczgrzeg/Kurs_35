import json
import logging
from monitoring import monitor

class FileHandler:
    def __init__(self, produkty_file, historia_file, saldo_file):
        self.produkty_file = produkty_file
        self.historia_file = historia_file
        self.saldo_file = saldo_file
        self.produkty = self.load_produkty_file()
        self.historia = self.load_historia_file()
        self.saldo = self.load_saldo_file()


    @monitor
    def load_produkty_file(self):
        with open(self.produkty_file) as file:
            return json.load(file)

    @monitor
    def load_historia_file(self):
        with open(self.historia_file) as file:
            return json.load(file)

    @monitor
    def load_saldo_file(self):
        with open(self.saldo_file) as file:
            saldo = file.read().strip()
            return float(saldo) if saldo else 0.0

    @monitor
    def save_produkty_file(self):
        with open(self.produkty_file, "w") as file:
            json.dump(self.produkty, file, indent=4)

    @monitor
    def save_historia_file(self):
        with open(self.historia_file, "w") as file:
            json.dump(self.historia, file, indent=4)

    @monitor
    def save_saldo_file(self):
        with open(self.saldo_file, "w") as file:
            file.write(str(self.saldo))

    def get_float_input(self, prompt):
        try:
            return float(input(prompt))
        except ValueError as e:
            print(" Wprowadzono nieprawidłową wartość (liczba zmiennoprzecinkowa).")
            logging.warning(f"Błąd konwersji do float: {e}")
            return None

    def get_int_input(self, prompt):
        try:
            return int(input(prompt))
        except ValueError as e:
            print(" Wprowadzono nieprawidłową wartość (liczba całkowita).")
            logging.warning(f"Błąd konwersji do int: {e}")
            return None


file_handler = FileHandler("produkty.json", "historia.json", "saldo.txt")


def save_temporary_data(file_handler, lista_produktow, saldo, historia):
    file_handler.produkty = lista_produktow
    file_handler.saldo = saldo
    file_handler.historia = historia
    file_handler.save_produkty_file()
    file_handler.save_saldo_file()
    file_handler.save_historia_file()