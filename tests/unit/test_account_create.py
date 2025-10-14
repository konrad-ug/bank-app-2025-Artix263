from src.account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
    def test_default(self):
        example_account=Account("Maciej","Dobrzyński")
        assert example_account.balance==0
