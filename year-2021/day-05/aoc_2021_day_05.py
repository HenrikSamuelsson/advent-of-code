'''
Solution to Advent of Code, year 2021, day 5.
'''

import os
from collections import defaultdict

file = 'input.txt'           # Name of the file with input data.
path = os.path.dirname(__file__)  # Path to the file with input data.
file_and_path = os.path.join(path, file)
input_file = open(file_and_path, 'r')

lines= input_file.readlines()

points = defaultdict(int)

for line in lines:
    line = line.replace(' -> ', ',')
    coords = [int(x) for x in line.split(',')]
    x1 = coords[0]
    x2 = coords[2]
    y1 = coords[1]
    y2 = coords[3]
    delta_x = x2 - x1
    delta_y = y2 - y1
    if delta_x != 0:
        k = delta_y / delta_x
    else:
        k = 666
    m = y1 - k * x1 
    
    print(k)
    
    if delta_x == 0:
        if (y2 > y1):
            for y in range(y1, y2 + 1):
                key = 'x' + str(x1) + 'y' + str(y)
                points[key] += 1
        else:
            for y in range(y2, y1 + 1):
                key = 'x' + str(x1) + 'y' + str(y)
                points[key] += 1
                
    elif delta_y == 0:
        if x2 > x1:
            for x in range(x1, x2 + 1):
                key = 'x' + str(x) + 'y' + str(y1)
                points[key] += 1
        else:
            for x in range(x2, x1 + 1):
                key = 'x' + str(x) + 'y' + str(y1)
                points[key] += 1
    
    elif delta_x > 0:
        y = y1
        for x in range(x1, x2 + 1):
            key = 'x' + str(x) + 'y' + str(y)
            points[key] += 1
            if y2 > y1:    
                y += 1
            else:
                y -= 1
    elif delta_x < 0:
        y = y2
        for x in range(x2, x1 + 1):
            key = 'x' + str(x) + 'y' + str(y)
            points[key] += 1
            if y2 > y1:
                y -= 1
            else:
                y += 1
             
print(points)
count = 0
for value in points.values():
    if value > 1:
        count += 1

print(count)
    