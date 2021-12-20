'''
Solution to Advent of Code, year 2021, day 6.

Works ok for part 1 but consumes to much resources for part 2.
'''
import os

FILE = 'test-input.txt'                # Name of the file with input data.
path = os.path.dirname(__file__)  # Path to the file with input data.
file_and_path = os.path.join(path, FILE)
input_file = open(file_and_path, 'r')

lines= input_file.readlines()

# Read in the comma separated number of lanternfish on the first line of input.
lanternfishes = [int(x) for x in lines[0].split(',')]

buckets = [0] * 10

SIMULATION_TIME = 255   # Use 80 for part 1
CREATION_TIME = 6
INITIAL_CREATION_TIME = 8


for fish in lanternfishes:
    buckets[fish] += 1

print (buckets)
    
for day in range(SIMULATION_TIME):
    for count in range(1, 10):
       buckets[count - 1] = buckets[count]
    buckets[9] = buckets[0]
    buckets[7] += buckets[0]
    #print(buckets)
    fish_count = sum(buckets[1:])
    #print(fish_count)
    print(day)

fish_count = sum(buckets[1:])
print(fish_count)
