import json
import os

class FileHandler:
    def __init__(self, file_path):
        self.file = file_path
        if not os.path.exists(self.file):
            with open(self.file, "w") as file:
                json.dump({}, file)
        self.data = self.read_data_from_file()

    def read_data_from_file(self):
        with open(self.file) as file:
            return json.load(file)

    def write_data_to_file(self):
        with open(self.file, "w") as file:
            json.dump(self.data, file, indent=4)

