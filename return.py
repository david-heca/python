# Funciones return en Python

def sumaRango(min, max):
    sum = 0
    for x in range(min, max):
        sum += x

    return(sum) # Nos devuelve ahora un valor en lugar de imprimirlo directamente

result = sumaRango(1, 11)
print(result) # Ahora nosotros decidimos si imprimirla o no

# ****** Multiples Returns y Args *******

def volume(length = 1, width = 2, depth = 3): # Podemos asignar valores por defecto en caso de no enviarlos
    return length * width * depth, width, 'Hola' # Ahora estamos retornando multiples valores (TUPLA)

result = volume(10, 20, 3)
print(result)

result = volume(width = 10) # Solo enviamos un valor
print(result)

print(result[0]) # También podemos pedir solo un return