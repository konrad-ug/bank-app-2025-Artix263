class Transfer:
    def transfer_lose(self,money):
        if self.balance>=money and money>0 :
            self.balance-=money
            
    def transfer_gain(self,money):
        if money>0:
            self.balance+=money