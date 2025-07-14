import json
import os

class FileHandler:
    def __init__(self, file_path):
        self.file = file_path
        if not os.path.exists(self.file):
            with open(self.file, "w") as file:
                json.dump({}, file)
        self.data = self.read_data_from_file()
        self.iterator = iter(self.data.items())


    def read_data_from_file(self):
        with open(self.file) as file:
            return json.load(file)

    def __getitem__(self, item):
        city, date = item
        return self.data.get(city, {}).get(date, "Data not found")

    def __setitem__(self, key, value):
        city, date = key
        if city in self.data.keys():
            self.data[city][date] = value
        else:
            self.data[city] = {}
            self.data[city][date] = value

    def write_data_to_file(self):
        with open(self.file, "w") as file:
            json.dump(self.data, file, indent=4)

    def items(self):
        for city, date_dict in self.data.items():
            for date_value, weather_info in date_dict.items():
                yield city, date_value, weather_info

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)