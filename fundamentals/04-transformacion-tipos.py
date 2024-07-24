# Transformación de tipos de datos en Python

nombre = "David" # str

nombre = 12 # int

nombre = False # bool

# la concatenación unicamente se puede hacer con los mismos tipos de datos
print("David" + " Herrera") # David Herrera
print(10 + 20) # 30

edad = 22
# print("Mi edad es: " + str(edad)) # cambiar de int -> str
print(f"Mi edad es: {edad}") # alternativa

# conversion explícita de tipos de datos (casting)
edad = int(input("Ingresa tu edad: \n"))
print(type(edad))