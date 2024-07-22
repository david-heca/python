# Comparación de números flotantes en Python

x = 3.3
y = 1.1 + 2.2
print(x == y) # Da False por la presición de cada variable

yStr = format(y, ".2g") # Aquí estamos cortando la presición con format
print("Str: " + yStr)

print(round(y,1)) # Otra manera de redondear
print(type(round(y,1)))

tolerance = 0.00001 # Usando una tolerancia
print(abs(x - y) < tolerance)