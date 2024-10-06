def fizz_buzz_sum(target):
  suma = 0
  for n in range(target):
    if (n % 3 == 0) or (n % 5 == 0):
      suma += n
  return suma
