import re
import os
 #load in all lines in array [line_index(i)][row_index(j)]

# 1- iterate lines, find number
# 2- find length of number
# 3 - check all suronding indexes for symbols
# 3.1 if found store number
# 4 return to 1 from end of number

#filepath= '/home/rj/codeing/Advent_of_code/3/engine_schematic'
filepath= os.path.os.path.dirname(os.path.realpath(__file__))+'/engine_schematic'

game_file = open(filepath, "r")
schematic = game_file.readlines()
game_file.close()

numbers = []
gears = []


def verify_number(line, start_index, end_index, number, max_line_length):
    #print("line: "+ str(line) +", start: "+ str(start_index) + " end: "+ str(end_index) + "number: "+ str(number))
    #find length of number:
    #check surounding indexes
    above_line = line-1 if line>0 else line
    below_line = line+2 if line<len(schematic)-1 else line +1
    before_index = start_index-1 if start_index>0 else start_index
    behind_index = end_index+1 if end_index<max_line_length-1 else end_index -1
    for i in range(above_line,below_line):
        for j in range(before_index, behind_index):
            if not schematic[i][j].isdigit() and schematic[i][j] != ".":
                numbers.append(int(number))
                return

def verify_gear(line, index, max_line_length):
    already_found_digets = []
    gear_numbers = []
    #print("line: "+ str(line) +", start: "+ str(start_index) + " end: "+ str(end_index) + "number: "+ str(number))
    #find length of number:
    #check surounding indexes
    above_line = line-1 if line>0 else line
    below_line = line+2 if line<len(schematic)-1 else line +1
    before_index = index-1 if index>0 else index
    behind_index = index+1 if index<max_line_length-1 else index -1
    for i in range(above_line,below_line):
        for j in range(before_index, behind_index):
            if schematic[i][j].isdigit():
                if (i,j) not in already_found_digets:
                    number_digets = [(i,j)]
                    left_pointer = -1
                    right_pointer = 1
                    # id all points in number
                    while schematic[i][j+ left_pointer].isdigit():
                        number_digets.insert(0, (i,j+left_pointer))
                        left_pointer = left_pointer -1
                    while schematic[i][j+right_pointer].isdigit():
                        number_digets.append((i,j+left_pointer))
                        right_pointer = 1+ right_pointer
                    # get number and add it to gear numbers
                    number = ""
                    for point in number_digets:
                        number =  number + schematic[int(point[0])][int(point[1])]
                    gear_numbers.append(int(number))
                    # add points of numbers to already_found
                    already_found_digets.extend(number_digets)

    # multiply gear numbers and add to gear array           
    if len(gear_numbers == 2):
        gear = gear_numbers[0] * gear_numbers[1]
        gears.append(gear)

#####Get numbers
# for line in range(len(schematic)):
#     for match in re.finditer(r'\d+', schematic[line]):
#         verify_number(line, match.start(), match.end(), match.group(), len(schematic[line]))
    

# print(numbers)
# print(sum(numbers))


#####Get gears
for line in range(len(schematic)):
    for match in re.finditer(r'[*]', schematic[line]):
        verify_gear(line, match.start(), len(schematic[line]))
    

print(gears)
print(sum(gears))
