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
    
    def add_car(self,*value):
        for car in value:
            if isinstance(car,Car):
                self.cars.append(car)
            else:
                print("Enter the machine")