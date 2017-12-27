import numpy

""" irrelevant example
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = []
for year in years_of_birth:
    ages.append(2014 - year)

print(ages)
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print('a')
print(a)

a_even=[]

i_even=0

for ia in a:
    if ia%2==0:
        a_even.append(ia)

print('a_even')
print(a_even)