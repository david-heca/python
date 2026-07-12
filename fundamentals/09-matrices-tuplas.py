# Matriz en Python
# Una matriz es una colección bidimensional de elementos, similar a una lista de listas

matriz = [  # Se declara una matriz
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matriz)
print(matriz[0])  # Imprimimos la primera fila
print(matriz[0][1])  # Imprimimos el segundo elemento de la primera fila

# Tuplas en Python
# Son una colección ordenada e inmutable de elementos

numbers = (1, 2, 3, 4, 5)  # Se declara con parentesís
print(type(numbers))

# ¿Cómo se accede a un valor?
print(numbers[0])

# numbers[0] = 10 # No se puede modificar

nombres = ("juan", "david", "andre")
print(nombres.index("david"))  # Si podemos consultar

# Una tupla se puede convertir en una lista
nueva = list(nombres)
print(type(nueva))

# Nota: También se pude transformar una lista a una tupla
