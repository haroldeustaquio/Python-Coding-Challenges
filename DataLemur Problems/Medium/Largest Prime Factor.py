def largest_prime_factor(target):
  
  lista=[]
  
  for n in range(1,target//2):
    if target%n==0:
      lista.append(n)
  
  lista_primo = []
  for x in lista:
    count=0
    for i in range(1,x+1):
      if x%i==0:
        count += 1
    if count==2:
      lista_primo.append(x)
  return max(lista_primo)