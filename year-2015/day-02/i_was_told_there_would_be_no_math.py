import re

file = open("input2015d02.txt")
data = file.read()
file.close()

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

print('Part One Answer: ' + str(total_paper_area))
