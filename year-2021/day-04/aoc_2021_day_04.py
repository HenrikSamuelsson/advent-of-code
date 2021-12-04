'''
Solution to Advent of Code, year 2021, day 4.
'''

import os

file = 'test-input.txt'           # Name of the file with input data.
path = os.path.dirname(__file__)  # Path to the file with input data.
file_and_path = os.path.join(path, file)
input_file = open(file_and_path, 'r')

lines= input_file.readlines()

# Read in the comma separated bingo numbers on the first line of input.
bingo_numbers = [int(x) for x in lines[0].split(',')]

print(bingo_numbers)

print(len(lines))

# Read in all the bingo boards.
bingo_boards = list()
for i in range(2, len(lines), 6):
    board = list()
    for j in range(i, i + 5):
        row = [int(x) for x in lines[j].split()]
        board.append(row)
    bingo_boards.append(board)

print(bingo_boards)

for number in bingo_numbers:
    # Strike out number if on board
    for bingo_boards_idx, bingo_board in enumerate(bingo_boards):
        for board_idx, board in enumerate(bingo_board):
            for row_idx, row in enumerate(board):
                if number == row:
                    bingo_boards[bingo_boards_idx][board_idx][row_idx] = -1

print('bingo')
