class Person:
    def __init__(self,name,last,year,passport):
        self.name = name
        self.last = last
        self.year = year
        self.passport = passport
        
    
    def get_info(self):
        return f"{self.name} {self.last} year of birth {self.year} passport number {self.passport}"
    
    def get_name(self):
        return self.name
    
    def get_last(self):
        return self.last
    
    
class Student(Shaxs):
    def __init__(self,name,last,year,passport,idnumber,address):
        super().__init__(self,name,last,year,passport)
        self.idnumber = idnumber
        self.address = address
        self.stage = 1
        
    def get_id(self):
        return self.idnumber
    
    def get_stage(self):
        return self.stage
    
    
class Address:
    def __init__(self,city,district,street,home):
        self.city = city
        self.district = district
        self.street = street
        self.home = home
        
    def get_address(self):
        return f"City {self.city}, district {self.district}, street {self.street}, {self.home}-lives at home."

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    