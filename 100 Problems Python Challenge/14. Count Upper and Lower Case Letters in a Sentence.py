# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

list_word = (input('Write some words: '))
list_word = list_word.replace(' ','')

list_word = list(list_word)

upper = 0
lower = 0

for letter in list_word:
    if (letter.isupper()):
        upper+=1
    elif letter.islower():
        lower+=1
print(f'UPPER: {upper}')
print(f'lower: {lower}')