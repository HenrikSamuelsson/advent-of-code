from os import path

file_path = path.relpath("year-2023/test-input.txt")
with open(file_path) as f:
    lines = f.read()

print(lines)
