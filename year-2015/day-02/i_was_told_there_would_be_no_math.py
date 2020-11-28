import re

# Get the puzzle input data that have been stored in a text file.
file = open("input2015d02.txt")
data = file.read()
file.close()

# Start of part one where total amount of paper is calculated.
total_paper_area = 0

for line in data.splitlines():
    # Parse out the present dimensions in int format from the line of data.
    dim = [int(s) for s in re.findall(r'\d+', line)]
    # Calculate each surface area of this present based on the dimensions.
    surface_areas = [dim[0] * dim[1], dim[0] * dim[2], dim[1] * dim[2]]
    # Calculate how much paper this present needs.
    paper_area = 2 * sum(list(surface_areas)) + min(list(surface_areas))
    # Update the total paper area.
    total_paper_area += paper_area

# Start of part two where total amount of ribbon is calculated
total_ribbon_length = 0

for line in data.splitlines():
    # Parse out the present dimensions in int format from the line of data.
    dim = [int(s) for s in re.findall(r'\d+', line)]
    # Sort the dimensions in ascending order.
    dim.sort()
    # Calculate how much ribbon this present needs, both for the wrapping and the bow.
    ribbon_length = 2 * (dim[0] + dim[1]) + dim[0] * dim[1] * dim[2]
    # Update the total ribbon length.
    total_ribbon_length += ribbon_length

print('Part one answer: ' + str(total_paper_area))
print('Part two answer: ' + str(total_ribbon_length))
