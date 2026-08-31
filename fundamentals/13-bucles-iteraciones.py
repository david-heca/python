# Ciclos: for en Python
# El ciclo for es un ciclo que se repite un número determinado de veces,  ideal si sabemos cuantas veces queremos que se repita el ciclo.

# for element in range(1, 21): # range(inicio, fin)
# 	print(element)

lista = [71, 2, 42, 13, 4]
for i in lista:  # uno por uno
    print(i)

tupla = ("David", "Julian", "Abraham")
for i in tupla:
    print(i)

dicc = {"nombre": "david", "apellido": "herrera", "edad": 22}
for i in dicc:  # itera naturalmente las keys
    print(i)

for i in dicc:
    print(dicc[i])  # imprime los valores de las keys

for key, value in dicc.items():
    print(key, "=", value)

personas = [
    {"nombre": "david", "edad": 23},
    {"nombre": "pepe", "edad": 13},
    {"nombre": "angelica", "edad": 30},
]

for persona in personas:
    print(persona)  # imprime cada diccionario de la lista

# Ciclos: WHILE en Python
# El ciclo while es un ciclo que se repite mientras una condición sea verdadera.

"""
while True: # mientras sea True
	print('Se ejecuto')


contador = 0
while contador < 10:
	contador += 1 # cada vez que se ejecute se suma uno
	print(contador)


contador = 0
while contador < 20:
	contador += 1
	if contador == 15:
		break # forza terminar el ciclo
	print(contador)
"""

contador = 0
while contador < 20:
    contador += 1
    if contador <= 15:
        continue  # si el contador es menor o igual a 15, se salta la iteración y no imprime nada pero sigue sumando hasta que llegue a 20
    print(contador)
