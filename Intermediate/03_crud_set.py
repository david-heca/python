# Modificando conjuntos en Python

set_countries = {'mex', 'col', 'per'}
size = len(set_countries) # Devuelve el no. de elementos del conjunto
print(size)

print('mex' in set_countries) # Evaluamos si esta mex en el conjunto

# insert
set_countries.add('bol') # Podemos agregar un elemento
print(set_countries)

# update
set_countries.update({'arg', 'ecu'}) # Estamos actualizando con otro conjunto
print(set_countries)

# delete
set_countries.remove('col') # Eliminar algún elemento
print(set_countries)

set_countries.discard('col') # Si no existe el elemento, no hace nada

set_countries.clear() # Limpia todo el conjunto => Vacío
print(set_countries)
