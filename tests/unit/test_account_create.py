from src.account import Account
from src.account import FirmAccount


class TestAccount:
    #Tests for feature 1 and 2 
    def test_account_creation(self):
        account = Account("John", "Doe","12345678912")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.pesel=="12345678912"
    #Tests for feature 3
    def test_pesel_too_long(self):
        account = Account("John", "Doe","1234567812912")
        assert account.pesel == "Invalid"
    def test_pesel_too_short(self):
        account = Account("John", "Doe","daw")
        assert account.pesel == "Invalid"
    #Tests for feature 4
    def test_promo_code_valid(self):
        account = Account("John", "Doe","64070867891","PROM_123")
        assert account.balance==50.0
    def test_promo_code_wrong_prefix(self):
        account = Account("John", "Doe","1234567812912","PRAM_ODW")
        assert account.balance == 0.0
    def test_promo_code_wrong_suffix(self):
        account = Account("John", "Doe","1234567812912","PROM_DWQ2")
        assert account.balance == 0.0
    def test_promo_code_wrong_format(self):
        account = Account("John", "Doe","1234567812912","PROjh")
        assert account.balance == 0.0
    #Tests for feature 5
    def test_promo_code_born_before_1960(self):
        account=Account("John","Doe","55031212345","PROM_123")
        assert account.balance==0.0
    def test_promo_code_born_after_2000(self):
        account=Account("John","Doe","04270812345","PROM_123")
        assert account.balance==50.0
    def test_promo_code_born_after_1960_before_2000(self):
        account=Account("John","Doe","64070867891","PROM_123")
        assert account.balance==50.0


class TestTransferMoney:
    def test_income_transfer(self):
        account = Account("John", "Doe","64070867891","PROM_123") #1. set up
        account.transfer_gain(150.0) # 2.action
        assert account.balance==200.0 # 3.assertion

    def test_income_transfer_negative_value(self):
        account = Account("John", "Doe","64070867891","PROM_123")
        account.transfer_gain(-20.0)
        assert account.balance==50.0

    def test_outcome_transfer(self):
        account = Account("John", "Doe","64070867891","PROM_123")
        account.transfer_lose(10.0)
        assert account.balance==40.0

    def test_outcome_transfer_bigger_than_balance(self):
        account = Account("John", "Doe","64070867891")
        account.transfer_lose(20.0)
        assert account.balance==0.0


    

class TestFirmAccount:
    def test_account_creation(self):
        account=FirmAccount("Januszex","1234567891")
        assert account.company_name=="Januszex"
        assert account.nip=="1234567891"
    def test_Nip_to_long(self):
        account=FirmAccount("Januszex","12345678911212")
        assert account.nip=="Niepoprawny NIP!"
    def test_Nip_to_short(self):
        account=FirmAccount("Januszex","4567891")
        assert account.nip=="Niepoprawny NIP!"


        

    
