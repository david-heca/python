# Strings avanzados en Python

nombre = "David"
apellido = "Herrera"

# Concatenación
nombreCompleto = nombre + " " + apellido
print(nombreCompleto)

quote = "I'm Nicolas" # Trabajando con diferentes comillas
print(quote)

# Manipulación del formato
template = "Mi nombre es " + nombre + " y mi apellido es " + apellido
print(template)

template2 = "Mi nombre es {}, y mi apellido es {}".format(nombre, apellido)
print(template2)

template3 = f"Mi nombre es {nombre}, y mi apellido es {apellido}"
print(template3)