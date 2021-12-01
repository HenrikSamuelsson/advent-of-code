import os

depths = list()

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as fobj:
   for line in fobj:
       depths.append(int(line.strip('\n')))

#print(depths)

last = depths[0]
increases = 0

for n in depths[1:]:
    if n > last:
        increases += 1
    last = n

# Answer to part 1
print(increases)

last_three = depths[0] + depths[1] + depths[2]
increases_three = 0

max_idx = len(depths) - 2
for i in range(1, max_idx):
    current_three = depths[i] + depths[i + 1] + depths[i + 2]
    if current_three > last_three:
        increases_three += 1
    last_three = current_three

print(increases_three)
