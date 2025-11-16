from src.FirmAccount import FirmAccount
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