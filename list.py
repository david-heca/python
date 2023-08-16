# List Comprehension en Python

numbers = [] 
for element in range(1, 11): # Agrega elementos a una lista (rango del 1 al 11)
    numbers.append(element * 2)
    
print(numbers)

numbers2 = [element * 2 for element in range(1, 11)] # Haz una lista más fácil con List Comp.
print(numbers2)

numbers3 = [i * 2 for i in range(1, 11) if i % 2 == 0] # Guarda los numeros pares en una lista
print(numbers3)
