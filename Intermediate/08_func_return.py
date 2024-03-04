# Funciones return en Python

def sumaRango(min, max):
    sum = 0
    for i in range(min, max):
        sum += i
    return(sum) # Retornamos el valor de la suma

result = sumaRango(1, 10)
print(result)

# ****** Multiples Returns y Args *******

def volume(length = 1, width = 2, depth = 3): # Podemos asignar valores por defecto en caso de no enviarlos
    return length * width * depth, width, 'Hola' # Ahora estamos retornando multiples valores (como TUPLA)

result = volume(10, 20, 3)
print(result)

result = volume(width = 10) # Solo enviamos un valor
print(result)

print(result[0]) # Como tupla podemos aplicar indexing para obtener el valor que queremos
