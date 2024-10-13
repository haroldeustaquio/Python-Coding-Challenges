def missing_int(input: list[int])-> int:
  if max(input)+1 == len(input):
    return max(input)+1
  else:
    lista = [n for n in range(max(input)+1) if n not in input]
    return lista
  