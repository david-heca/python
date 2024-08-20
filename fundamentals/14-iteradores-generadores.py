# Iteradores en Python

lista = [1, 2, 3]

iterador = iter(lista) # Creamos un iterador a partir de la lista

print(next(iterador)) # next() nos permite obtener el siguiente elemento de la lista
print(next(iterador))
print(next(iterador))
# print(next(iterador))

# texto = "Hola mundo"
# iterador = iter(texto)

# for char in range(len(texto)):
# 	print(next(iterador)) # podemos iterar sobre el texto

limite = 10
iterador = iter(range(1, limite + 1, 2)) # iterador de un rango de 1 a 10 con saltos de 2

for i in iterador:
	print("Iterador:", i)

# Generadores en Python
# Un generador es una función que nos permite obtener valores sobre la marcha, es decir, no se almacenan en memoria todos los valores, sino que se van generando conforme se necesitan.

# def generador():
#     yield 1 # yield permite devolver un valor y pausar la ejecución de la función
#     yield 2 # al llamar nuevamente a la función, la ejecución se reanuda
#     yield 3 # y se devuelve el siguiente valor

# for valor in generador():
# 	print(valor)

# Fibonacci: se trata de una secuencia de números en la que cada número es la suma de los dos anteriores. Por ejemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fibonacci(limite):
    a, b = 0, 1
    while a < limite:
        yield a
        a, b = b, a + b

for valor in fibonacci(10):
	print(valor)
