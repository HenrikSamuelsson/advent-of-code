from os import path

# Look up the path to the file holding input data.
file_path = path.relpath("year-2023/test-input.txt")

# Open the input file and read in all the lines in it.
with open(file_path) as input_file:
    lines = input_file.read()


print(lines)
