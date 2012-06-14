def desigualdadKraft(k, longitudes):
  """Esta funcion devuelve True si se cumple la desigualdad de Kraft
     y False en caso contrario."""
  total = 0.0
  for lng in longitudes:
    total += pow(k, -lng)

  if total <= 1.0:
    return True
  return False

def igualdadKraft(k, longitudes):
  """Esta funcion devuelve True si se cumple la igualdad de Kraft
     y False en caso contrario."""
  total = 0.0
  for lng in longitudes:
    total += pow(k, -lng)

  if total == 1.0:
    return True
  return False

def main():
  """Podemos probar como funcionan las funciones previas
     descomentando los valores para longitudes y imprimiendo
     el resultado de la funcion."""
  longitudes = [1]
  #longitudes = [1, 1, 1]
  #longitudes = [1, 1]
  k = 2
  
  print igualdadKraft(k, longitudes)

if __name__ == "__main__":
  main()

