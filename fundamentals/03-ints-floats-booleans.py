# Números en Python

vidas = 3
print(type(vidas)) # int

temperatura = 12.2
print(type(temperatura)) # float

temperatura = 4e2 # notación científica
print(temperatura)

valor = 3.14159
print("Valor: {:.2f}".format(valor)) # redondeo a 2 decimales

vidas = vidas - 1 # reutilizamos valor
print(vidas)

# Calculadora de presupuesto promedio
presEne = input("Ingresa tu presupuesto de Enero: \n")
presFeb = input("Ingresa tu presupuesto de Febrero: \n")
presMar = input("Ingresa tu presupuesto de Marzo: \n")

promedio = (int(presEne) + int(presFeb) + int(presMar)) / 3
print(f"Tu promedio es de: {promedio} por mes")

# Booleans en Python

soltero = True
print(type(soltero)) # bool
print(soltero)

print(not soltero) # not: invierte el estado de la variable