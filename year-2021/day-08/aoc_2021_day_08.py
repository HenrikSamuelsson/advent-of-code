'''
Solution to Advent of Code, year 2021, day 8.
'''
import os

FILE = 'input.txt'                # Name of the file with input data.
path = os.path.dirname(__file__)  # Path to the file with input data.
file_and_path = os.path.join(path, FILE)
input_file = open(file_and_path, 'r')

lines = input_file.readlines()

digit_count = [0] * 10

for line in lines:
    split_line = line.split('|')  # Split the patterns and digits apart.
    digits = split_line[1].split()
    for digit in digits:
        if len(digit) == 2:
            digit_count[1] += 1
        elif len(digit) == 4:
            digit_count[4] += 1
        elif len(digit) == 3:
            digit_count[7] += 1
        elif len(digit) == 7:
            digit_count[8] += 1

print(sum(digit_count))
