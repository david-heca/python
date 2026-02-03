class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.available = True

    def sell(self):
        if not self.is_available:
            self.is_available = True
            print("Vehículo venidido correctamente")
        else:
            print(
                f"El vehículo {self.brand} - {self.model} se encuentra de nuevo disponible"
            )

    def buy(self) -> bool:
        if self.is_available:
            self.is_available = False
            print("Vehículo comprado correctamente")
            return True
        else:
            print(f"El vehículo {self.brand} - {self.model} no se encuentra disponible")
            return False

    def check_availability(self):
        return self.is_available

    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")


class Car(Vehicle):
    def start_engine(self):
        if self.is_available:
            return f"El motor del vehículo {self.brand} - {self.model} está en marcha"
        else:
            return f"El vehículo {self.brand} - {self.model} no está disponible"

    def stop_engine(self):
        if self.is_available:
            return f"El motor del vehículo {self.brand} - {self.model} se ha detenido"
        else:
            return f"El vehículo {self.brand} - {self.model} no está disponible"


class Bike(Vehicle):
    def start_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} - {self.model} está en marcha"
        else:
            return f"La bicicleta {self.brand} - {self.model} no está disponible"

    def stop_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} - {self.model} se ha detenido"
        else:
            return f"La bicicleta {self.brand} - {self.model} no está disponible"


class Truck(Vehicle):
    def start_engine(self):
        if self.is_available:
            return f"El motor del camión {self.brand} - {self.model} está en marcha"
        else:
            return f"El camión {self.brand} - {self.model} no está disponible"

    def stop_engine(self):
        if self.is_available:
            return f"El motor del camión {self.brand} - {self.model} se ha detenido"
        else:
            return f"El camión {self.brand} - {self.model} no está disponible"


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            vehicle.buy()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"El vehículo {self.brand} - {self.model} no está disponible")

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            availability = "disponible"
        else:
            availability = "no disponible"
        print(
            f"El vehículo {self.brand} - {self.model} se encuentra {availability} y cuesta {vehicle.price}"
        )

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
                    print(
                        f"{vehicle.brand} - {vehicle.model} por {vehicle.get_price()}"
                    )
