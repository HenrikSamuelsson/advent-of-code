import os

file = 'test-input.txt'  # Name of the file with input data.
path = os.path.dirname(__file__)
file_and_path = os.path.join(path, file)

position = 0
depth = 0

aim = 0
position_part_2 = 0
depth_part_2 = 0

with open(file_and_path, 'r') as fobj:
    for line in fobj:
        input = line.split()
        if input[0] == 'forward':
            position += int(input[1])
            position_part_2 += int(input[1])
            depth_part_2 += aim * int(input[1])
        if input[0] == 'down':
            depth += int(input[1])
            aim += int(input[1])
        if input[0] == 'up':
            depth -= int(input[1])
            aim -= int(input[1])

# Answer for part 1.
print (position * depth)

# Answer for part 2.
print (position_part_2 * depth_part_2)