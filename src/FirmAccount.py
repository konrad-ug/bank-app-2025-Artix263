from src.transfer import Transfer


class FirmAccount(Transfer):
    def __init__(self,company_name,nip):
        self.company_name=company_name
        self.nip=nip if self.nip_validation(nip) else "Niepoprawny NIP!"
        self.balance=0.0
    def nip_validation(self,Nip):
        if len(Nip)==10:
            return True
        return False
    def transfer_express(self,value_money):
        if value_money>0 and self.balance+5>=value_money:
            self.balance-=value_money+5
            
        
