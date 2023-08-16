# Funciones Lambda en Python

def increment(x):
    return x + 1

result = increment(10)
print(result)

increment2 = lambda x : x + 1 # La misma función pero en lambda

result2 = increment2(10)

print(result2)

fullname = lambda name, lastName : f'Tu numbe completo es {name.title()} {lastName.title()}'

print(fullname('David', 'Herrera'))