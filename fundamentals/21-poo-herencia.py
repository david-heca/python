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