# Transformación de tipos de datos en Python

# Ejemplo de como podemos cambiar el tipo de dato de una variable de manera dinamica
nombre = "David" # String
print(type(nombre))

nombre = 12 # Integer
print(type(nombre))

nombre = False
print(type(nombre))

# La concatenación unicamente se puede hacer en los mismos tipos de datos
print("David" + " Herrera") # David Herrera
print(10 + 20) # 30

# Es necesario hacer uso de los mismos tipos de datos
edad = 22
# print("Mi edad es: " + str(edad)) # Cambiar de int -> str
print(f"Mi edad es: {edad}")

# Aqui se convierte directamente el input a int
edad = int(input("Ingresa tu edad: \n"))
print(type(edad))