# Dictionary Comprehension en Python
import random

dict = {}
for i in range(1, 5):
    dict[i] = i * 2 # Creamos un diccionario donde su valor va a ser el doble de la key

print(dict)

dict2 = {i : i * 2 for i in range(1, 5)} # Con Dict. Comprehension (key : value)
print(dict2)

countries = ['col', 'mex', 'bol'] # Lista de países
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

print("****** Condicionales ******")

result = {country : population for (country, population) in population2.items() if population > 50} # Si la población es mayor a 20
print(result)

text = 'Hola, soy david'
unique = {c : text.count(c) for c in text if c in 'aeiou'} # Obtenemos la vocal y la guardamos el numero de veces que hay en el texto
print(unique)
