from os import path
import re

# Look up the path to the file holding input data.
file_path = path.relpath("year-2023/puzzle-input.txt")

# Open the input file and read in all the lines in it.
with open(file_path) as input_file:
    lines = input_file.readlines()

total_points = 0

for line in lines:
    line = line.replace('|', ':')
    # Split input line into three parts:
    # 0. string holding card identifier
    # 1. string holding winning numbers
    # 2. string holding numbers that we have
    parts = re.split(':', line)

    # Strip away some white space from the strings.
    stripped_parts = [part.strip() for part in parts]

    # Put the winning numbers in a list.
    winning_numbers = [int(i) for i in stripped_parts[1].split()]

    # Put our numbers in a list.
    our_numbers = [int(i) for i in stripped_parts[2].split()]

    # Count how many winning numbers we have.
    match_count = 0
    for our_number in our_numbers:
        if our_number in winning_numbers:
            match_count += 1

    # Calculate how many points this card gives us.
    points = 0
    if match_count > 0:
        points = 2 ** (match_count - 1)

    # Update total number of points from all cards.
    total_points += points

# Print answer for part 1.
print(total_points)
