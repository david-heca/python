# Operadores aritmeticos en Python
# PEMDAS: Parentesis, Exponenciales, Multiplicación/División, Adición/Sustracción

print(10 + 10)
print(10 - 10)
print(10 * 10)
print(10 / 10)  # siempre devuelve un float
print(3**2)  # potenciación
print(10 % 3)  # modulo: es el residuo de una división
print(10 // 3)  # división entera: devuelve la parte entera de la división

# Nota: el modulo puede ayudar a saber si un número es par o impar

# Operadores de comparación en Python
# Devuelven como resultado un valor booleano (True o False)

# > Mayor que
print(7 > 3)

# < Menor que
print(8 < 10)

# >= Mayor o igual
print(2 >= 2)

# <= Menor o igual
print(3 <= 10)

# == Igualdad
print(2 == 4)

# != Desigualdad o diferente
print(9 != 10)

print("Apple" == "apple")  # False
print(1 == "1")  # False

# Operadores de asignación en Python
# Permiten asignar valores a variables y realizar operaciones al mismo tiempo

a = 5

a += 3  # a = a + 3
print(a)
a -= 2  # a = a - 2
print(a)
a *= 2  # a = a * 2
print(a)
a /= 2  # a = a / 2
print(a)

# Walrus operator (operador morsa) disponible a partir de Python 3.8
# Permite asignar un valor a una variable dentro de una expresión
print(b := 10)  # Asigna 10 a b y luego imprime el valor de b
