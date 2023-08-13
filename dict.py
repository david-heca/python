# Dictionary Comprehension en Python

dict = {}
for i in range(1, 5):
    dict[i] = i * 2 # Creamos un diccionario donde su valor va a ser el doble de la key

print(dict)

dict2 = {i : i * 2 for i in range(1, 5)} # Con Dict. Comprehension
print(dict2)

import random
countries = ['col', 'mex', 'bol'] # Asignamos población a cada país
population = {}
for country in countries:
    population[country] = random.randint(1, 100) # Aleatorio

print(population)

population2 = {country : random.randint(1, 100) for country in countries} # Versión corta
print(population2)

names = ['nico', 'david', 'santi']
ages = [19, 23, 25]

print(list(zip(names, ages))) # zip: une las listas

# par clave-valor que viene del iterable de una lista con tuplas
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)

# ****** Condicionales ******

result = {country : population for (country, population) in population2.items() if population > 20} # Si la población es mayor a 20
print(result)

result2 = {}
for (country, population) in population2.items():
    result2[country] = population

print(result2)

text = 'Hola, soy david'
unique = {c : text.count(c) for c in text if c in 'aeiou'} # Obtenemos la vocal y la guardamos el numero de veces que hay en el texto
print(unique)