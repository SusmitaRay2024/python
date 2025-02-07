class Car: 
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def display_info(self):
        print(f"Car make: {self.make}, model: {self.model}")
        
car = Car("Toyota", "Corolla")
car.display_info()