# Funciones dentro de otras funciones

def increment(x):
    return x + 1

def hofunct(x, func): # Hacemos uso de una funcion como parámetro
    return x + func(x)

result = hofunct(2, increment) # Pasamos la funcion como argumento
# 2 + (2 + 1) = 5
print(result)

# También se puede hacer con las funciones lambda

increment2 = lambda x : x + 1

hofunct2 = lambda x, func : x + func(x)

result2 = hofunct2(2, increment2)
print(result2)