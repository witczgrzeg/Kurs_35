import sys
from file_handler import FileHandler

argumenty = sys.argv[1:]

file_handler = FileHandler(
    input_file_path=argumenty[0],
    output_file_path=argumenty[1],
    transformations=argumenty[2:]
)

file_handler.make_transformations()
print(file_handler.data)
file_handler.save_data()