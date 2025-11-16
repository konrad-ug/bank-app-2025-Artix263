class Account:
    def __init__(self):
        self.history=[]
    def transfer_lose(self,money):
        if self.balance>=money and money>0 :
            self.history.append(-money)
            self.balance-=money

    def transfer_gain(self,money):
        if money>0:
            self.history.append(money)
            self.balance+=money
    def transfer_express(self,money,fee):
        if money>0 and self.balance+fee>=money:
            self.history.append(-money)
            self.history.append(-fee)
            self.balance-=money+fee
