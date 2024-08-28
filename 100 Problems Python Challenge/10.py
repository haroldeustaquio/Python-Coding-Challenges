# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

list_word = input('Write some words: ').split(' ')

from collections import defaultdict

temp_dict = defaultdict(int)
for word in list_word:
    temp_dict[word] += 1

temp_list = list(temp_dict.keys())

temp_list.sort()

','.join(temp_list)