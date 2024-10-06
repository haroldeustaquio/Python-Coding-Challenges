def trailing_zeroes(n):
  temp=1
  for i in range(1,n+1):
    temp *= i
  
  count = 0
  while temp%10 ==0:
      count+=1
      temp=temp//10
  
  return count
