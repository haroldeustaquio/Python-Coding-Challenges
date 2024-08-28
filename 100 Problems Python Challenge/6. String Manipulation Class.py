# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

import math
C = 50
H = 30

Ds = input('Write list of numbers: ').split(' ')
Qs = []

for D in (Ds):
    Qs.append(str(round(math.sqrt((2*C*int(D))/H))))

print(','.join(Qs))