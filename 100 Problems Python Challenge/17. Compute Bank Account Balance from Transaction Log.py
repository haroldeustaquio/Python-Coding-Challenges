# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

from collections import defaultdict
list_trans = defaultdict(float)

while True:
    transaction = input('Write some words: ').split(' ')
    
    if transaction == ['']:
        break
    else: 
        list_trans[transaction[0]] += int(transaction[1])
        
list_trans['D'] - list_trans['W']