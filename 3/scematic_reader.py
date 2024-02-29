import re
 #load in all lines in array [line_index(i)][row_index(j)]

# 1- iterate lines, find number
# 2- find length of number
# 3 - check all suronding indexes for symbols
# 3.1 if found store number
# 4 return to 1 from end of number


filepath= '/home/rj/codeing/Advent_of_code/3/engine_schematic'

game_file = open(filepath, "r")
schematic = game_file.readlines()
game_file.close()

numbers = []


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

def verify_gear(line, row):
    pass

for line in range(len(schematic)):
    #for match in re.finditer(r'\d+', schematic[line]):
    #    verify_number(line, match.start(), match.end(), match.group(), len(schematic[line]))
    for match in re.finditer(r'[*]', schematic[line]):
        print(match)

print(sum(numbers))
