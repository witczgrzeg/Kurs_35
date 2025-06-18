import csv

class FileHandler:
    def __init__(self, input_file_path, output_file_path):
        self.input_file = input_file_path
        self.output_file = output_file_path
        self.data = self.load_data()
    def load_data(self):
        with open(self.input_file) as file:
            reader = csv.reader(file)
            temp_matrix = []
            for row in reader:
                temp_row = []
                for value in row:
                    temp_row.append(value)
            temp_matrix.append(temp_row)
        return temp_matrix