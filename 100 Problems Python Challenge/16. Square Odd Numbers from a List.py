# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9


list_word = (input('Write some words: ')).split(',')
new_list = []
for word in list_word:
    if(int(word)%2 != 0):
        new_list.append(str(int(word)**2))
        
print(','.join(new_list))