# Funciones Lambda en Python

def increment(x): # Función que incrementa un valor en 1
    return x + 1

result = increment(10)
print(result) # 11

increment = lambda x : x + 1 # La misma función pero en lambda (entrada : salida)

result2 = increment(10)
print(result2)

fullname = lambda name, lastName : f'Tu numbe completo es {name} {lastName}'

print(fullname('David', 'Herrera'))
