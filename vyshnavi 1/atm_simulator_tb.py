import unittest
from atm_simulator import BankAccount, ATM


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("1234", 10000)

    def test_check_balance(self):
        self.assertEqual(self.account.check_balance(), 10000)

    def test_deposit(self):
        result = self.account.deposit(5000)

        self.assertTrue(result)
        self.assertEqual(self.account.check_balance(), 15000)

    def test_invalid_deposit(self):
        result = self.account.deposit(-100)

        self.assertFalse(result)
        self.assertEqual(self.account.check_balance(), 10000)

    def test_withdraw(self):
        result = self.account.withdraw(3000)

        self.assertTrue(result)
        self.assertEqual(self.account.check_balance(), 7000)

    def test_insufficient_balance(self):
        result = self.account.withdraw(15000)

        self.assertFalse(result)
        self.assertEqual(self.account.check_balance(), 10000)

    def test_invalid_withdraw(self):
        result = self.account.withdraw(-500)

        self.assertFalse(result)
        self.assertEqual(self.account.check_balance(), 10000)


class TestATM(unittest.TestCase):

    def setUp(self):
        self.atm = ATM()

    def test_valid_pin(self):
        account = self.atm.authenticate("1234")

        self.assertIsNotNone(account)
        self.assertEqual(account.check_balance(), 10000)

    def test_invalid_pin(self):
        account = self.atm.authenticate("9999")

        self.assertIsNone(account)

    def test_second_account(self):
        account = self.atm.authenticate("5678")

        self.assertIsNotNone(account)
        self.assertEqual(account.check_balance(), 5000)


if __name__ == "__main__":
    unittest.main(verbosity=2)