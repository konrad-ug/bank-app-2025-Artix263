class Account:
    def __init__(self, first_name, last_name,pesel,promotional_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance= 50.0 if self.is_promo_code_valid(promotional_code) and self.is_promo_code_age_valid(pesel)  else 0.0
        self.pesel=pesel if self.is_pesel_valid(pesel) else "Invalid"
        
        
    def is_pesel_valid(self,pesel):
        if len(pesel)==11 and pesel.isdigit():
            return True
        return False 
    
    def is_promo_code_valid(self,promotial_code):
        if (promotial_code == None):
            return False
        if (len(promotial_code) !=8):
            return False
        correct="PROM_"
        for i in range(0,5):
            if promotial_code[i]!=correct[i]:
                return False
        return True
    def is_promo_code_age_valid(self,pesel):
        year=int(pesel[0]+pesel[1])
        month=int(pesel[2]+pesel[3]) ##In pesel third and fourth number cover month,range of numbers depends on century .For example 2000-2099 have range for months 21-32
        if (year>60 and 0<=month<=12) or (21<=month<=32 and year<=25) : ##If we import date we could track current year for valid year infromation (can't have year from future)
            return True
        else:
            return False

