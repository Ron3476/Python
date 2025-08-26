# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number} 📞")

    def info(self):
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB")

# Child class inheriting from Smartphone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)  # Inherit parent constructor
        self.gpu = gpu

    # Polymorphism: overriding info() method
    def info(self):
        print(f"Gaming Phone: {self.brand} {self.model}, Storage: {self.storage}GB, GPU: {self.gpu}")

# Creating objects
phone1 = Smartphone("Samsung", "S25", 256)
phone2 = GamingPhone("Asus", "ROG 8", 512, "Adreno X2")

# Using methods
phone1.info()
phone1.call("+254700123456")

phone2.info()
phone2.call("+254711987654")

#polymorphism
class Vehicle:
    def move(self):
        pass  # placeholder method

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
