import numpy as np

def distinct_number(numbers):
    tmp_numbers = {}
    for number in numbers:
        key = str(number)
        if key in tmp_numbers:
            tmp_numbers[key] = tmp_numbers[key] + 1
        else:
            tmp_numbers[key] = 1
            
    max_val = [x for x in tmp_numbers.keys() if tmp_numbers[x] == max(tmp_numbers.values())]
    if len(max_val) > 0:
        return int(max_val[0])
    return 'NO_RESULT'

array = np.array([0, 5, 4, 0, 4, 4, 3, 4, 0, 0, 4, 5, 2, 1, 1, 9])
max_repeated_number = distinct_number(array)

max_repeated_number