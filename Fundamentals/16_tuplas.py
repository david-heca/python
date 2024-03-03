# Tuplas en Python, son tipos de datos inmutables, es decir, no se pueden modificar, eliminar o agregar elementos

numbers = (1,2,3,4,5) # Se declara con parentesís
nombres = ('juan', 'david', 'andre')

print(type(numbers))

# ¿Cómo se accede a un valor?
print(numbers[0])
print(numbers[-1])

print(nombres.index('david')) # Si podemos consultar

# Una tupla se puede convertir en una lista
nueva = list(nombres)
print(type(nueva))

# NOTA: También se pude transformar una lista a una tupla