# Funciones Lambda en Python

# Las funciones lambda son funciones anónimas que se pueden utilizar para realizar operaciones sencillas y rápidas. Se definen con la palabra clave lambda, seguida de los parámetros y dos puntos, y a continuación la operación a realizar.

add = lambda a, b: a + b # (entrada : salida)
print(add(5, 3))  # 8

numbers = range(11)
square = list(map(lambda x: x ** 2, numbers)) # map() aplica una función a cada elemento de una lista
print(square)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # filter() filtra los elementos de una lista que cumplan con una condición
print(even_numbers)