'''
Solution to Advent of Code, year 2021, day 6.
'''
import os

FILE = 'input.txt'                # Name of the file with input data.
path = os.path.dirname(__file__)  # Path to the file with input data.
file_and_path = os.path.join(path, FILE)
input_file = open(file_and_path, 'r')

lines= input_file.readlines()

# Read in the comma separated number of lanternfish on the first line of input.
lanternfishes = [int(x) for x in lines[0].split(',')]

SIMULATION_TIME = 256
CREATION_TIME = 6
INITIAL_CREATION_TIME = 8

for day in range(SIMULATION_TIME):
    number_of_new_lantern_fish = 0
    for fish_index, fish in enumerate(lanternfishes):
        if fish == 0:
            lanternfishes[fish_index] = CREATION_TIME
            number_of_new_lantern_fish += 1
        else:
            lanternfishes[fish_index] -= 1
    for new_fish in range(number_of_new_lantern_fish):
        lanternfishes.append(INITIAL_CREATION_TIME)
    #print(day)
    #print(lanternfishes)
    #print(len(lanternfishes))

fish_count = len(lanternfishes)
print(fish_count)
