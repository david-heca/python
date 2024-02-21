# Numbers en Python

vidas = 3 # Así se declara un numero como variable
print(type(vidas))

presupuesto = 100.00 # Numeros flotantes o float
temperatura = 12.2

print(type(temperatura))

vidas = vidas - 1 # Reutilizamos valor, se puede usar también con +
print(vidas)

vidas -= 1 # Reutilizamos valor
print(vidas)

print("Reto clase Numeros")

# Calcula el gasto de ciertos meses (ener, ebrero y marzo) y obtiene el promedio
presEne = input("Ingresa tu presupuesto de Enero: \n")
presFeb = input("Ingresa tu presupuesto de Febrero: \n")
presMar = input("Ingresa tu presupuesto de Marzo: \n")

promedio = (int(presEne) + int(presFeb) + int(presMar)) / 3

print(f"Tu promedio es de: {promedio} por mes")