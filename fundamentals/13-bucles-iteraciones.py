# Ciclos: for en Python
# El ciclo for es un ciclo que se repite un número determinado de veces,  ideal si sabemos cuantas veces queremos que se repita el ciclo.

# for element in range(1, 21): # range(inicio, fin)
# 	print(element)

lista = [71, 2, 42, 13, 4]
for i in lista: # uno por uno
	print(i)

tupla = ('David', 'Julian', 'Abraham') # tambien se puede iterar tuplas
for i in tupla:
	print(i)

dicc = {
	'nombre': 'david',
	'apellido': 'herrera',
	'edad': 22
}
for i in dicc: # itera naturalmente las keys
	print(i)

for i in dicc: # aqui los valores
	print(dicc[i])

for key, value in dicc.items():
	print(key, '=', value)

personas = [
	{
		'nombre': 'david',
		'edad': 23
	},
	{
		'nombre': 'pepe',
		'edad': 13
	},
	{
		'nombre': 'angelica',
		'edad': 30
	}
   ]

for persona in personas:
	print(persona) # Imprime cada persona dentro de la lista de diccionarios

# Ciclos: WHILE en Python
# El ciclo while es un ciclo que se repite mientras una condición sea verdadera.

'''
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
'''

contador = 0
while contador < 20:
	contador += 1
	if contador <= 15:
		continue # salta la logica posterior al continue y vuelve a iterar
	print(contador)