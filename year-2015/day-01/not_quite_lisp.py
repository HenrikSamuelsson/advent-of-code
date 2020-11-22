file = open("input2015d01.txt")
data = file.read()
file.close()

floor = 0
for direction in data:
    if direction == "(":
        floor += 1
    else:
        floor -= 1

print(floor)
