from src.PersonalAccount import PersonalAccount
from src.FirmAccount import FirmAccount


class TestAccount:
    #Tests for feature 1 and 2 
    def test_account_creation(self):
        account = PersonalAccount("John", "Doe","12345678912")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.pesel=="12345678912"
    #Tests for feature 3
    def test_pesel_too_long(self):
        account = PersonalAccount("John", "Doe","1234567812912")
        assert account.pesel == "Invalid"
    def test_pesel_too_short(self):
        account = PersonalAccount("John", "Doe","daw")
        assert account.pesel == "Invalid"
    #Tests for feature 4
    def test_promo_code_valid(self):
        account = PersonalAccount("John", "Doe","64070867891","PROM_123")
        assert account.balance==50.0
    def test_promo_code_wrong_prefix(self):
        account = PersonalAccount("John", "Doe","1234567812912","PRAM_ODW")
        assert account.balance == 0.0
    def test_promo_code_wrong_suffix(self):
        account = PersonalAccount("John", "Doe","1234567812912","PROM_DWQ2")
        assert account.balance == 0.0
    def test_promo_code_wrong_format(self):
        account = PersonalAccount("John", "Doe","1234567812912","PROjh")
        assert account.balance == 0.0
    #Tests for feature 5
    def test_promo_code_born_before_1960(self):
        account=PersonalAccount("John","Doe","55031212345","PROM_123")
        assert account.balance==0.0
    def test_promo_code_born_after_2000(self):
        account=PersonalAccount("John","Doe","04270812345","PROM_123")
        assert account.balance==50.0
    def test_promo_code_born_after_1960_before_2000(self):
        account=PersonalAccount("John","Doe","64070867891","PROM_123")
        assert account.balance==50.0


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


        

    
