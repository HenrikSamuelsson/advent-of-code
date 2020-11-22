file = open("input2015d01.txt")
data = file.read()
file.close()

floor = 0
basement_found = False
first_basement_position = 0
current_position = 0

for direction in data:
    if direction == "(":
        floor += 1
    else:
        floor -= 1
    current_position += 1
    if not basement_found and floor == -1:
        first_basement_position = current_position
        basement_found = True

print('Part One Answer: {}'.format(floor))
print('Part Two Answer: {}'.format(first_basement_position))
