phone_number = int(input())

temp_number = phone_number # Will be used to hold shifted amount

line_number = temp_number % 10000 # Rightmost 4 digits
temp_number = temp_number // 10000 # Shift right by 4 digits

prefix_number = temp_number % 1000 # Rightmost 3 digits
temp_number   = temp_number // 1000 # Shift right by 3 digits

area_code_number = temp_number # Remaining 3 digits are the area code

output = '(' + str(area_code_number) + ') ' + str(prefix_number) + '-' + str(line_number)
print(output)
