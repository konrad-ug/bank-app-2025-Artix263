from src.PersonalAccount import PersonalAccount
from src.FirmAccount import FirmAccount



class TestTransferMoney:
    def test_income_transfer(self):
        account = PersonalAccount("John", "Doe","64070867891","PROM_123") #1. set up
        account.transfer_gain(150.0) # 2.action
        assert account.balance==200.0 # 3.assertion

    def test_income_transfer_negative_value(self):
        account = PersonalAccount("John", "Doe","64070867891","PROM_123")
        account.transfer_gain(-20.0)
        assert account.balance==50.0

    def test_outcome_transfer(self):
        account = PersonalAccount("John", "Doe","64070867891","PROM_123")
        account.transfer_lose(10.0)
        assert account.balance==40.0

    def test_outcome_transfer_bigger_than_balance(self):
        account = PersonalAccount("John", "Doe","64070867891")
        account.transfer_lose(20.0)
        assert account.balance==0.0

    def test_outcome_transfer_negative_value(self):
        account = PersonalAccount("John", "Doe","64070867891","PROM_123")
        account.transfer_lose(-20.0)
        assert account.balance==50.0
    #Testes for express transfer outcome
    def test_express_outcome_correct_fee(self):
        account1 = PersonalAccount("John", "Doe","64070867891","PROM_123")
        account2=FirmAccount("Januszex","1234567891")
        account2.balance=1000.0
        account1.transfer_express(10)
        account2.transfer_express(100)
        assert account1.balance==39.0
        assert account2.balance==895.0

    def test_express_outcome_negative_value(self):
        account2=FirmAccount("Januszex","1234567891")
        account2.balance=1000.0
        account2.transfer_express(-20)
        assert account2.balance==1000.0

    def test_express_outcome_negative_balance_after_fee(self):
        account2=FirmAccount("Januszex","1234567891")
        account1 = PersonalAccount("John", "Doe","64070867891","PROM_123")
        account2.balance=1000.0
        account2.transfer_express(1000.0)
        account1.transfer_express(50.0)
        assert account2.balance==(-5.0)
        assert account1.balance==(-1.0)

    def test_express_outcome_transfer_bigger_than_saldo(self):
        account1 = PersonalAccount("John", "Doe","64070867891","PROM_123")
        account1.transfer_express(100.0)
        assert account1.balance==50.0

    def test_express_outcome_negative_balance_after_fee_not_max(self):
        account2=FirmAccount("Januszex","1234567891")
        account2.balance=1000.0
        account2.transfer_express(999.0)
        assert account2.balance==(-4.0)