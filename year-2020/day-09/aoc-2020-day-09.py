file = open("input.txt")
data = file.read()
file.close()

numbers = list()
for line in data.splitlines():
    numbers.append(int(line))

# Preamble is 5 in the test input and 25 in the real problem.
preamble_size = 25

for i in range(preamble_size, len(numbers)):
    current_numbers = (numbers[i - preamble_size:i])
    next_number = numbers[i]
    #print(current_numbers)
    #print('next_number ' + str(next_number))
    #print()
    number_is_ok = False
    for index_1 in range(0, len(current_numbers) - 1):
        nr_1 = current_numbers[index_1]
        #print('nr_1 = ' + str(nr_1))
        #print()
        for index_2 in range(1 + index_1, len(current_numbers)):
            nr_2 = current_numbers[index_2]
            #print('nr_2 = ' + str(nr_2))
            if ((nr_1 != nr_2) and (nr_1 + nr_2 == next_number)):
                number_is_ok = True
        #print()
    #print()
    if (not number_is_ok):
        index_of_failed_number = i
        failed_number = next_number
        print('This number failed: ' + str(failed_number))

for i in range(index_of_failed_number):
    #print(numbers[i])
    sum = numbers[i]
    for j in range(1 + i, index_of_failed_number):
        sum += numbers[j]
        if (sum == failed_number):
            start_index = i
            stop_index = j
            print('match ' + str(i) + ' ' + str(j))
        #print(numbers[j])
    #print()

smallest = min(numbers[start_index:stop_index + 1])
largest = max(numbers[start_index:stop_index + 1])
answer_2 = smallest + largest
print('answer_2 ' + str(answer_2));