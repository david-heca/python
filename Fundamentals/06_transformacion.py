# Transformación de tipos de datos en Python

# Ejemplo de como podemos cambiar el tipo de dato de una variable de manera dinamica
nombre = "David" # String

nombre = 12 # Integer

nombre = False

# La concatenación unicamente se puede hacer en los mismos tipos de datos
print("David" + " Herrera") # David Herrera
print(10 + 20) # 30

# Es necesario hacer uso de los mismos tipos de datos
edad = 22
# print("Mi edad es: " + str(edad)) # Forma de cambiar de int -> str
print(f"Mi edad es: {edad}") # Otra forma de hacerlo

# Aqui se convierte directamente el input a int
edad = int(input("Ingresa tu edad: \n"))
print(type(edad))