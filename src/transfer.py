class Transfer:
    def transfer_lose(self,money):
        if self.balance>=money and money>0 :
            self.balance-=money

    def transfer_gain(self,money):
        if money>0:
            self.balance+=money
    def transfer_express(self,value_money,fee):
        if value_money>0 and self.balance+fee>=value_money:
            self.balance-=value_money+fee