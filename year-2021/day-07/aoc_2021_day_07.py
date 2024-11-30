'''
Solution to Advent of Code, year 2021, day 7.
'''
import os
import statistics

FILE = 'input.txt'                # Name of the file with input data.
path = os.path.dirname(__file__)  # Path to the file with input data.
file_and_path = os.path.join(path, FILE)
input_file = open(file_and_path, 'r')

lines= input_file.readlines()

# Read in the comma separated horizontal positions on the first line of input.
positions = [int(x) for x in lines[0].split(',')]

# Calculate the median position using a library function.
median_position = statistics.median(positions)

fuel = 0
for position in positions:
    fuel += abs(position - median_position)

# Answer to part 1.
print(fuel)
