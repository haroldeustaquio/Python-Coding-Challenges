def max_three(input):
  lista = []
  for i in range(len(input)-2):
    for j in range(i+1,len(input)-1):
      for k in range(j+1,len(input)):
        prod = input[i]*input[j]*input[k]
        lista.append(prod)
        
  return max(lista)
