class Shaxs:
    def ___init__(self,ism,familiya,tyil,pasport):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.pasport = pasport
        
    
    def get_info(self):
        return f"{self.ism} {self.familiya}" 
        return f"{self.tyil}-yilda tug'ilgan Passport raqami{self.pasport}"
    
    def get_name(self):
        return self.ism
    
    def get_last(self):
        return self.familiya
    
    
class Talaba(Shaxs):
    def __init__(self,ism,familiya,tyil,pasport,idraqam,manzil):
        super().__init__(self,ism,familiya,tyil,pasport)
        self.idraqam = idraqam
        self.bosqich = 1
        
    def get_id(self):
        return self.idraqam
    
    def get_bosqich(self):
        return self.bosqich
    
    
class Manzil:
    def __init__(self,shaxar,tuman,kocha,uy):
        self.shaxar = shaxar
        self.tuman = tuman
        self.kocha = kocha
        self.uy = uy
        
    def get_manzil(self):
        return f"{self.shaxar} viloyati, {self.tuman} tumani, "
        return f"{self.kocha} ko'chasi, {self.uy}-uyda yashaydi."

talaba_manzil = Manzil("Andijon", "Qo'rg'ontepa", "Yakka chinor", 15)
talaba1 = Talaba("Bahodirjon", "Ikromov", 2006, "N0000012", "0101012", talaba_manzil)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    