# Diccionarios en Python
# Los diccionarios son una estructura que almacenan dos datos, la clave y el valor en donde podemos almacenar diferentes tipos de datos.

dicc = {
    "nombre": "david",  # key: value
    "apellido": "herrera",
    "edad": 22,
}

print(type(dicc))
print(len(dicc))  # conocer el numero de elementos
print(dicc["edad"])  # podemos obtener un valor de la key

print(dicc.get("edad2"))  # si no existe la key, devuelve None

# Inserción y actualización
dicc2 = {
    "nombre": "david",
    "apellido": "herrera",
    "lenguajes": [
        "Pyhton",
        "JS",
    ],  # podemos almacenar listas dentro de un diccionario
    "edad": 22,
}

dicc2["nombre"] = "aaron"  # podemos cambiar un valor
dicc2["lenguajes"].append("Rust")  # podemos trabajar con la lista dentro del dicc
print(dicc2)

del dicc2["apellido"]  # eliminar un atributo
dicc2.pop("edad")  # eliminar con pop
print(dicc2)

print("********* items *********")  # devuelve cada elemento
print(dicc2.items())

print("********* keys *********")  # devuelve los keys
print(dicc2.keys())

print("********* values *********")  # Devuelve directamente los valores
print(dicc2.values())
