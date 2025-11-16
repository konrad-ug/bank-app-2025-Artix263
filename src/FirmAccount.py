from src.Account import Account


class FirmAccount(Account):
    def __init__(self,company_name,nip):
        super().__init__()
        self.company_name=company_name
        self.nip=nip if self.nip_validation(nip) else "Niepoprawny NIP!"
        self.balance=0.0
        self.account_fee=5.0
    def nip_validation(self,Nip):
        if len(Nip)==10:
            return True
        return False
    def transfer_express(self,value_money):
        super().transfer_express(value_money,self.account_fee)
            
        
