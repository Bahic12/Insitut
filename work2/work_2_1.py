from uuid import uuid4

class Car:
    __num_car = 0
    def __init__(self,make,model,color,year,price,km=0):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.__km = km
        self.__id = uuid4()
        Car.__num_car += 1 
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_car
    
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        if km>0:
            self.__km += km
        else:
            print("The mileage of the car cannot be reduced")
            
    def __str__(self):
        return f"{self.make} {self.model} Year of manufacture {self.year}"
    
    def __eq__(self,y):
        return self.narh == y.narh
    
    def __lt__(self,y):
        return self.narh < y.narh
    
    def __le__(self,y):
        return self.narh > y.narh
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        