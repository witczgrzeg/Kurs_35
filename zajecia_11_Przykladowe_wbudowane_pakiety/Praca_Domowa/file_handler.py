import csv

class FileHandler:
    def __init__(self, input_file_path, output_file_path, transformations):
        self.input_file = input_file_path
        self.output_file = output_file_path
        self.data = self.load_data()
        self.transformations = transformations

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

    def save_data(self):
        with open(self.output_file, "w", newline='') as file:
            writer = csv.writer(file)
            for row in self.data:
                writer.writerow(row)

    def make_transformations(self):
        for transformation in self.transformations:
            transformation_list = transformation.split(",")
            x_str = transformation_list[0]
            y_str = transformation_list[1]
            wartosc = transformation_list[2]

            x = int(x_str)
            y = int(y_str)

            self.data[y][x] = wartosc
