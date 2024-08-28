# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

num_list = []
for num in range(2000,3000):
    if((num%7==0 )& (num%5!=0)):
        num_list.append(str(num))

print(','.join(num_list))