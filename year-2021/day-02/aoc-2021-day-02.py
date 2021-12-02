import os

file = 'input.txt'  # Name of the file with input data.
path = os.path.dirname(__file__)
file_and_path = os.path.join(path, file)

position = 0
depth = 0

with open(file_and_path, 'r') as fobj:
    for line in fobj:
        print(line.rstrip())
        input = line.split()
        print(input)
        if input[0] == 'forward':
            position += int(input[1])
        if input[0] == 'down':
            depth += int(input[1])
        if input[0] == 'up':
            depth -= int(input[1])

# Answer for part 1.
print (position * depth)
