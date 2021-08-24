from work_2_1 import Car

class CarSalon:
    def __init__(self,name):
        self.name = name
        self.cars = []
        
    def __repr__(self):
        return f"{self.name} salon"
    
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self,index):
        return self.cars[index]
    
    def __setitem__(self,index,value):
        self.cars[index] = value
    
    def __call__(self,*value):
        if value:
            for car in value:
               self.add_car(car)
        else:
            return [car for car in self.cars]
        
    def __add__(self,y):
        if isinstance(y, CarSalon()):
            new_salon = CarSalon(f"{self.name} {y.name}")
            new_salon.cars = self.cars + y.cars
            return new_salon
        elif isinstance(y,Car):
            self.add_car(y)
    
    def add_car(self,*value):
        for car in value:
            if isinstance(car,Car):
                self.cars.append(car)
            else:
                print("Enter the machine")
                
