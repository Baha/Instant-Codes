# devuelve True si se cumple la desigualdad de Kraft
# y False en caso contrario
def desigualdadKraft(k, longitudes):
  total = 0.0
  for lng in longitudes:
    total += pow(k, -lng)

  if total <= 1.0:
    return True
  return False

def igualdadKraft(k, longitudes):
  total = 0.0
  for lng in longitudes:
    total += pow(k, -lng)

  if total == 1.0:
    return True
  return False

def main():
  longitudes = [1]
  #longitudes = [1, 1, 1]
  #longitudes = [1, 1]
  k = 2
  
  print igualdadKraft(k, longitudes)

if __name__ == "__main__":
  main()

