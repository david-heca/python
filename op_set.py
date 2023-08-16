# Operaciones de conjuntos en Python

set_a = {'col', 'mex', 'bol'}
set_b = {'per', 'arg', 'mex'}

# Union: Todos
set_c = set_a.union(set_b) # Con método
print('Union:', set_c)

print('Union:', set_a | set_b) # Con operador

# Intersection: En común
set_c = set_a.intersection(set_b)
print('Intersection:', set_c)

print('Intersection:', set_a & set_b) 

# Difference: Remueve los elementos del segundo conjunto (incluyendo los comúnes)
set_c = set_a.difference(set_b)
print('Difference:', set_c)

print('Difference:', set_a - set_b)

# Symmetric Difference: Muestra lso elementos de ambos conjuntos (excluyendo los comúnes)
set_c = set_a.symmetric_difference(set_b)
print('Sym. Difference:', set_c)

print('Sym. Difference:', set_a ^ set_b)
