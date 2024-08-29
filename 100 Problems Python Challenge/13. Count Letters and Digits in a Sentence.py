# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

list_word = (input('Write some words: '))
list_word = list_word.replace(' ','')

list_word = list(list_word)

num = 0
let = 0

for letter in list_word:
    if (letter.isnumeric()):
        num+=1
    elif letter.isalpha():
        let+=1
print(f'LETTERS: {let}')
print(f'NUMBERS: {num}')