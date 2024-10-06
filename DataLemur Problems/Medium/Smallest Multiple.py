def smallest_multiple(target):
  prod = 1
  for i in range(1,target+1):
    prod*=i
  
  for n in range(1,prod+1):
    ver = 0
    for j in range(1,target+1):
      if n%j == 0:
        ver+=1
    if ver==target:
      return n
