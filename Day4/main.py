import numpy as np
file_path = "Day4\data.txt"

# Part1
def inrange(np_arr):
    if np_arr[0][0] >= np_arr[1][0] and np_arr[0][1] <= np_arr[1][1] or np_arr[0][0] <= np_arr[1][0] and np_arr[0][1] >= np_arr[1][1]:
        return 1
    else:
        return 0

# Part2
def full_inrange(np_arr):
    if np_arr[0][0] <= np_arr[1][0] and np_arr[1][0] <= np_arr[0][1] or np_arr[1][0] <= np_arr[0][0] and np_arr[0][0] <= np_arr[1][1]:
        return 1
    else:
        return 0


sum_1, sum_2 = 0, 0
with open(file_path) as file:
    for line in file:
        line = line.strip()
        x = line.split(',')
        x = [item.split('-') for item in x]
        x = np.array(x, dtype="int")
        sum_1 += inrange(x)
        sum_2 += full_inrange(x)

print(str(sum_1) + ' ' + str(sum_2))

"""
References:
Stijn Verhoeven
"""