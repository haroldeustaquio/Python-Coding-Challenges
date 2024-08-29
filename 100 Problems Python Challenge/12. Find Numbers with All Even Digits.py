# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

list_num = []

for x in range(2000,3000+1):
    temp=0
    x_temp = x
    for i in range(len(str(x))):
        if(x_temp%2==0):
            temp=temp+1
        x_temp = x_temp // 10

    if temp==4:
        list_num.append(x)

list_num