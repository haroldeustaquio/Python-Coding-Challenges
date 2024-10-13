def intersection(a, b):
  lista = []
  
  for na in a:
    if na in b:
      lista.append(na)
  
  return lista
