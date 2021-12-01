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

print(increases)
