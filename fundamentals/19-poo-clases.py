# Clases en Python

class Person():
    # __init__ es el constructor de la clase y su funcion principal es inicializar los objetos de una clase cuando se crean
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # geet es una funcion propia de la clase, la cual se le conoce como método
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")

# person1 = Person("David", 24)
# person1.greet()

class BankAccount():
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual {self.balance}.")
        else:
            print("No se puede realizar la operación. Cuenta inactiva.")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                print(f"Se ha retirado {amount}. Saldo actual {self.balance}.")
            else:
                print(f"Ingresa una cantidad menor a {self.balance}.")
        else:
            print("No se puede realizar la operación. Cuenta inactiva.")

    def status_account(self, status):
        if status:
            self.is_active = True
            print("Cuenta activada exitosamente")
        else:
            self.is_active = False
            print("Cuenta desactivada exitosamente")


account = BankAccount("David", 5000)
account.deposit(2000)
account.withdraw(10000)
account.withdraw(5000)
account.status_account(False)
account.deposit(2000)