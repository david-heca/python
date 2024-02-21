# Ciclos anidados en Python
matriz = [ # Una lista con varias listas
  [1,2,3], 
  [4,5,6], 
  [7,8,9]
]

print(matriz[0][1]) # Fila, Columna, imprimimos independientemente

for row in matriz:
  print(row) # Imprime toda la fila
  for column in row: # Entramos a los valores dentro de cada fila
    print(column) # Imprime cada elemento de esa fila