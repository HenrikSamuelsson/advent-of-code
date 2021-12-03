import os

file = 'input.txt'  # Name of the file with input data.
path = os.path.dirname(__file__)  # Path to the file with input data.
file_and_path = os.path.join(path, file)

# number_length = 5  # Length of test input is 5.
number_length = 12  # Length of real puzzle input is 12.

one_count = [0] * number_length  # Tracks the number of ones at each position.
zero_count = [0] * number_length  # Tracks the number of zeroes at each position.

with open(file_and_path, 'r') as input_file:
    for line in input_file:
        binary_chars = list(line)
        for idx in range(number_length):
            if  binary_chars[idx] == '1':
                one_count[idx] += 1
            else:
                zero_count[idx] += 1

print (one_count)
print (zero_count)

gamma = 0
epsilon = 0

for idx in range(number_length):
    if (one_count[number_length - 1 - idx] > zero_count[number_length - 1 - idx]):
        gamma += 2 ** idx
    else:
        epsilon += 2 ** idx

print (gamma)
print (epsilon)
print (gamma * epsilon)  # The power of the motor, answer to part 1.
