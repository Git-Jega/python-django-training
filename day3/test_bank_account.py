import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Alice", 100)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), "Current balance: $100")

    def test_deposit(self):
        result = self.account.deposit(50)
        self.assertEqual(result, "Successfully deposited $50 to your account.")
        self.assertEqual(self.account.get_balance(), "Current balance: $150")

    def test_deposit_invalid(self):
        result = self.account.deposit(0)
        self.assertEqual(result, "Deposit amount must be positive.")

    def test_withdraw(self):
        result = self.account.withdraw(30)
        self.assertEqual(result, "Successfully withdrew $30 from your account.")
        self.assertEqual(self.account.get_balance(), "Current balance: $70")

    def test_withdraw_insufficient(self):
        result = self.account.withdraw(200)
        self.assertEqual(result, "Insufficient balance.")

    def test_withdraw_invalid(self):
        result = self.account.withdraw(0)
        self.assertEqual(result, "Withdraw amount must be positive.")

if __name__ == '__main__':
    unittest.main()
