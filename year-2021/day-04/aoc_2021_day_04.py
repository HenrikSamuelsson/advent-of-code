'''
Solution to Advent of Code, year 2021, day 4.
'''

import os

file = 'input.txt'           # Name of the file with input data.
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

bingo = False
for number in bingo_numbers:
    # Strike out number if on board
    for bingo_boards_idx, bingo_board in enumerate(bingo_boards):
        for board_idx, board in enumerate(bingo_board):
            for row_idx, row in enumerate(board):
                if number == row:
                    bingo_boards[bingo_boards_idx][board_idx][row_idx] = -1

    for bingo_boards_idx, bingo_board in enumerate(bingo_boards):
        for row_idx, row in enumerate(bingo_board):
            # Check rows for bingo
            bingo_on_row = True
            for row_value_idx, row_value in enumerate(row):
                if row_value != -1:
                    bingo_on_row = False
                    break
            if bingo_on_row:
                bingo = True

        # Check columns for bingo
        for col_idx in range(5):
            bingo_on_col = True
            for row_idx in range(5):
                current_num = bingo_boards[bingo_boards_idx][row_idx][col_idx]
                if bingo_boards[bingo_boards_idx][row_idx][col_idx] != -1:
                    bingo_on_col = False
            if bingo_on_col:
                bingo = True
