def max_subarray_sum(input):
  sumas=[]
  for i in range(len(input)-1):
    temp_suma = input[i]
    for j in range(i+1,len(input)):
      temp_suma += input[j]
      if temp_suma < 0:
        sumas.append(0)
      else:
        sumas.append(temp_suma)
  return max(sumas)
