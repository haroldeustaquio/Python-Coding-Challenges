# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

upper_list = []

while True:
    list_word = input('Write some words: ').split(' ')
    if list_word != ['']:
        [upper_list.append(word.upper()) for word in list_word]
    else: 
        break

print(' '.join(upper_list))