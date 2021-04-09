import numpy as np

def unique_numbers(numbers):
    tmp_array = []
    for number in numbers:
        if number not in tmp_array:
            tmp_array.append(number)
    return tmp_array

unique_number_list = unique_numbers(np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]))

unique_number_list