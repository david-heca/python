# Modificando conjuntos

set_countries = {'mex', 'col', 'per'}
size = len(set_countries) # Devuelve el no. de elementos del conjunto (tamaño)
print(size)

print('mex' in set_countries) # Evaluamos si esta mex en el conjunto

# add
set_countries.add('bol') # Podemos agregar un elemento
print(set_countries)

# update
set_countries.update({'arg', 'ecu'}) # Estamos actualizando con otro conjunto
print(set_countries)

# delete
set_countries.remove('col') # Eliminar algún elemento
print(set_countries)

set_countries.discard('col') # Cómo manejar un elemento que no existe?: Lo descartamos (No da error)
print(set_countries)

# Limpia todo el conjunto => Vacío
set_countries.clear()
print(set_countries)
