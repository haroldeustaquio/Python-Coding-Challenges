import math

def mean(x):
    return sum(x) / len(x)

def sd(x):
    m = mean(x)
    ss = sum((i - m) ** 2 for i in x)
    return math.sqrt(ss / len(x))

def corr(x, y):
    # Cambiar 'sum' a un nombre de variable que no sea palabra clave
    sum_product = 0
    for i in range(len(x)):
        sum_product += (x[i] - mean(x)) * (y[i] - mean(y))
    
    return sum_product / len(x) / (sd(x) * sd(y))
