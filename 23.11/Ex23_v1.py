import numpy

with open('happynumbers.txt') as open_file:
    happynumbers_list = open_file.read()
happynumbers_list = happynumbers_list.split()
# print(happynumbers_list)

with open('primenumbers.txt') as open_file:
    primeNums_list = open_file.read()
primeNums_list = primeNums_list.split()
# print(primeNums_list)

common_nums = []
for item in happynumbers_list:
     if item in primeNums_list:
        common_nums.append(item)

print(common_nums)
# print(primeNums_list)
# print(happynumbers_list)