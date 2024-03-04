# Higher Order Functions (HOF) en Python

# Las HOF son funciones que toman una o más funciones como argumentos y/o devuelven una función como resultado.
def increment(x):
    return x + 1

def hofunct(x, func): # Hacemos uso de una funcion como parámetro
    return x + func(x)

result = hofunct(2, increment) # Pasamos la funcion como argumento
print(result) # 2 + (2 + 1) = 5

# También se puede hacer con las funciones lambda

increment2 = lambda x : x + 1 # (entrada : salida)

hofunct2 = lambda x, func : x + func(x)

result2 = hofunct2(2, increment2)
print(result2)