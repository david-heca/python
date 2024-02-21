# Tuplas en Python, son tipos de datos INMUTABLES

numbers = (1,2,3,4,5) # Se declara con parentesís
nombres = ('juan', 'david', 'andre')

print(type(numbers)) 

# ¿Cómo se accede a un valor?
print(numbers[0])
print(numbers[-1])

# En una tupla solo vamos a poder declarar valores, no se pueden modificar o eliminar
print(nombres.index('david')) # Si podemos consultar

# Si podemos transformar
nueva = list(nombres) # Ahora la tupla normbres es una lista
print(type(nueva))
print(nueva)

# NOTA: También se pude transformar una lista a una tupla