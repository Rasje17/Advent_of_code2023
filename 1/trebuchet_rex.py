import regex as re

number_lookup = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9",}

def getnumber(number) -> int:
    if number.isdigit():
        return number
    else:
        return number_lookup.get(number)


    return 0



filepath = "/home/rj/codeing/Advent_of_code/1/calibrations"

typed_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "\d"]

pattern = r"({})".format('|'.join(typed_numbers))

number_array = []

cali_file = open(filepath, "r")

lines = cali_file.readlines()

for line in lines:
    
    all_numbers = re.findall(pattern, line, overlapped=True)

    #print(all_numbers)
    
    
    cal_numbers = getnumber(all_numbers[0]) + getnumber(all_numbers[-1])

    number_array.append(int(cal_numbers))
#   print(cal_numbers)


cali_file.close()
print(sum(number_array))



