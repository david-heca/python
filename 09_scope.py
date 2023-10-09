# Scope en Python

price = 100 # scope global dentro del archivo

def increment():
    price = 200 # scope local, dentro de la función unicamente

    return price

print(price)
print(increment())
