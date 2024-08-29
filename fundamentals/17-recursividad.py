# Recursividad en Python
# Recursividad es una técnica en programación donde una función se llama a sí misma para resolver un problema.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))

def suma_digitos(n):
    # Caso base: si n es menor que 10, significa que tiene un solo dígito
    if n < 10:
        return n
    else:
        # Caso recursivo: suma el último dígito con la suma de los demás dígitos
        return n % 10 + suma_digitos(n // 10)