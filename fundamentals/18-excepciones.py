# Excepciones en Python

# try:
    # Podría causar error
# except TipoDeError:
    # Se ejecutará si ocurre un error

try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
except ValueError:
    print("Debes introducir un número entero")
except ZeroDivisionError:
    print("No se puede dividir por cero")

# else
    # Se ejecuta si no ocurre ninguna excepción.
# finally
    # Se ejecuta siempre, ocurra o no una excepción, y se usa para liberar recursos o realizar tareas de limpieza.

archivo = None

try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("No se puede dividir por cero")
else:
    print("División exitosa")
finally:
    resultado = 0

# 'pass' es una declaración nula en Python. Se usa como un marcador de posición cuando una declaración es obligatoria sintácticamente, pero no quieres que haga nada.

def funcion_no_implementada():
    pass  # Aquí no pasa nada, pero el código es válido

