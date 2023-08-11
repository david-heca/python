# Conjuntos/Sets en Python

# no tiene un par key-value, así me doy cuenta que es un set, un conjunto
set_countries = {'mex', 'col', 'per'}
print(type(set_countries))

set_types = {1, 'hola', False, 12.4} # Un conjunto puede tener diferentes tipos
print(set_types)

set_from_string = set('holaaa') # Crea un conjunto a partir de la palabra 'Hola'
print(set_from_string) # !!!: Al imprimir se eliminan elementos duplicados

set_from_tuples = set(('abc','cbv','as'))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
set_numbers= set(numbers) # Cremos un conjunto a partir de una lista
print(set_numbers)

unique_numbers = list(set_numbers) # Pasamos el conjunto al tipo: lista
print(unique_numbers)