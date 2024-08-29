# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

a = int(input('Write a digit: '))

string='a+aa+aaa+aaaa'
string_list = string.replace('a',str(a)).split('+')

sum = 0
for num in string_list:
    sum+=int(num)

sum