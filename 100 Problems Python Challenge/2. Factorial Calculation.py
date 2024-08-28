# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:

n = int(input('Write a num: '))

prod = 1
for i in range(1,n+1):
    prod *= i

print(prod)