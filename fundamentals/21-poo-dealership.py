# Dealership

# compra y venta de vehiculos, caber cuales estan disponibles y su precio

class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if not self.is_available:
            self.is_available = True
            print("Vehículo venidido correctamente")
        else:
            print (f"El vehículo {self.brand} - {self.model} se encuentra de nuevo disponible")

    def buy(self) -> bool:
        if self.is_available:
            self.is_available = False
            print("Vehículo comprado correctamente")
            return True
        else:
            print (f"El vehículo {self.brand} - {self.model} no se encuentra disponible")
            return False

    def check_availability(self):
        return self.is_available
    
    def get_price(self):
        return self.price

class Client:
    def __init__(self, name, client_id):
        self.name = name
        self.client_id = client_id
        self.vehicles = []

    def sell_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            vehicle.sell()
            self.vehicles.remove(vehicle)
        else:
            print ("No cuentas con este vehiculo para vender")

    def buy_vehicle(self, vehicle):
        if vehicle.buy():
            self.vehicles.append(vehicle)
            
    def inquire_vehicle(self, vehicle):
        availability = "disponible" if vehicle.check_availability() else "no disponible"
        print(f"El vehículo {vehicle.brand} - {vehicle.model} está {availability}, precio: {vehicle.price}")

class Dealership:
    def __init__(self):
        self.vehicles = []
        self.clients = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"El vehiculo {vehicle.brand} - {vehicle.model} ha sido agregado")

    def register_client(self, client):
        self.clients.append(client)
        print(f"El cliente {client.name} ha sido registrado")

    def show_available_vehicles(self):
        print("Vehículos disponibles:")
        for vehicle in self.vehicles:
            if vehicle.is_available:
                print(f"{vehicle.brand} - {vehicle.model} por {vehicle.get_price()}")

vehicle1 = Vehicle("Mazda", "Mazda 3", 1500)
vehicle2 = Vehicle("Toyota", "Corolla", 1800)
vehicle2 = Vehicle("Nissan", "Sentra", 1750)

client1 = Client("David", "001")

dealership = Dealership()
dealership.register_client(client1)
dealership.add_vehicle(vehicle1)
dealership.add_vehicle(vehicle2)

dealership.show_available_vehicles()

client1.inquire_vehicle(vehicle1)

client1.buy_vehicle(vehicle1)

dealership.show_available_vehicles()

client1.sell_vehicle(vehicle1)

client1.sell_vehicle(vehicle2)

dealership.show_available_vehicles()