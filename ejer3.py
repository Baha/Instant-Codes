def sucChar(caracter, alfabeto):
  """Esta funcion devuelve el simbolo sucesor de un caracter
     en un alfabeto dado."""
  if caracter == alfabeto[-1]:
    return alfabeto[0]
  else:
    devolver = False
    for car in alfabeto:
      if devolver == True:
        return car
      if car == caracter:
        devolver = True

def sucStr(cadena, alfabeto):
  """Esta funcion devuelve la cadena sucesora de una cadena
     en un alfabeto dado."""
  if cadena[-1] == alfabeto[-1]:
    return (sucStr(cadena[:-1],alfabeto) + sucChar(cadena[-1], alfabeto))
  else:
    return cadena[:-1] + sucChar(cadena[-1], alfabeto)
    
def main():
  """En esta funcion podemos comprobar como funcionan los
     anteriores modulos, consiguiendo codigos instantaneos
     con las propiedades especificadas."""
  alfabeto = ['0', '1']
  longitudes = [1, 2, 3, 4, 4]
  #alfabeto = ['0', '1']
  #longitudes = [4, 4, 4, 4]
  codificaciones = []

  codificaciones.append(longitudes[0] * alfabeto[0])
  
  i = 1
  while i < len(longitudes):
    codificaciones.append(sucStr(codificaciones[i-1],alfabeto) + ((longitudes[i] - longitudes[i-1]) * alfabeto[0]))
    i = i + 1

  print codificaciones

if __name__ == "__main__":
  main()

