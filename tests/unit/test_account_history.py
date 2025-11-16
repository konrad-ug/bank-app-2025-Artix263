from src.FirmAccount import FirmAccount

class TestTransferHistory:
    def test_correct_transfer_gain_in_history(self):
        account=FirmAccount("Januszex","1234567891")
        account.transfer_gain(500.0)
        assert 500 in account.history
    def test_correct_transfer_lose_in_history(self):
        account=FirmAccount("Januszex","1234567891")
        account.balance=400.0
        account.transfer_lose(300)
        assert -300.0 in account.history
    def test_correct_transfer_express_in_history(self):
        account=FirmAccount("Januszex","1234567891")
        account.balance=400.0
        account.transfer_express(200)
        assert -200.0 in account.history and -5.0
    def test_insufficent_balance_to_withdrow_no_record_in_history(self):
        account=FirmAccount("Januszex","1234567891")
        account.transfer_express(300)
        assert -300 not in account.history