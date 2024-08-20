# Funciones en Python

# def greet(name, last_name = "No tiene apellido"):  # 'name' es el parámetro
#     print("Hola", name, last_name)

# greet("David", "Herrera")  # "David" es el argumento

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    return a / b

def calculator():
    while True:
        print("Bienvenido a la calculadora")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        option = int(input("Ingresa una opción: "))

        if option == 5:
            print("¡Hasta luego!")
            break
        if option in [1, 2, 3, 4]:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            if option == 1:
                print("Resultado:", add(a, b))
            elif option == 2:
                print("Resultado:", substract(a, b))
            elif option == 3:
                print("Resultado:", multiply(a, b))
            elif option == 4:
                print("Resultado:", divide(a, b))
        else:
            print("Opción no válida")

calculator()