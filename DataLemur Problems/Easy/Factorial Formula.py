def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        prod = n * factorial(n-1)
    return prod
