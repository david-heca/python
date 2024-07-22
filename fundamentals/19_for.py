# Ciclos: for en Python

# El ciclo for es un ciclo que se repite un número determinado de veces, es decir, se repite un número finito de veces, es ideal si sabemos cuantas veces queremos que se repita el ciclo.
for element in range(1, 21): # range(inicio, fin)
  print(element)

lista = [71,2,42,13,4]
for i in lista: # Estamos iterando bajo un conjunto dado, uno por uno
  print(i)

tupla = ('David', 'Julian', 'Abraham') # Tambien se puede iterar tuplas
for i in tupla:
  print(i)

dicc = {
  'nombre': 'david',
  'apellido': 'herrera',
  'edad': 22
}
for i in dicc: # Itera naturalmente las keys
  print(i)

for i in dicc: # Ahora los valores
  print(dicc[i])

for key, value in dicc.items():
  print(key, '=', value)

personas = [ # Lista de diccionarios
  {
    'nombre': 'david',
    'edad': 23
  },
  {
    'nombre': 'pepe',
    'edad': 13
  },
  {
    'nombre': 'angelica',
    'edad': 30
  }
]

for persona in personas:
  print(persona) # Imprime cada persona dentro de la lista de diccionarios