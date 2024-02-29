import re
filepath = "/home/rj/codeing/Advent_of_code/1/calibrations"

number_array = []

cali_file = open(filepath, "r")

lines = cali_file.readlines()

for line in lines:
    all_numbers= ''.join(x for x in line if x.isdigit())
    cal_numbers = all_numbers[0] + all_numbers[-1]

    number_array.append(int(cal_numbers))

    #print(cal_numbers)


cali_file.close()
print(sum(number_array))



