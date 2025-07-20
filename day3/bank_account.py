import random

class BankAccount:
    bank_accounts = []

    def __init__(self, name, balance=0):
        self.__account_number = random.randint(10**11, (10**12) - 1)
        self.__account_holder_name = name
        self.__balance = balance
        BankAccount.bank_accounts.append(self)

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.__balance += amount
        return f"Successfully deposited ${amount} to your account."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdraw amount must be positive."
        if amount > self.__balance:
            return "Insufficient balance."
        self.__balance -= amount
        return f"Successfully withdrew ${amount} from your account."

    def get_balance(self):
        return f"Current balance: ${self.__balance}"

def main():
    while True:
        print("\n1) Create a new bank account\n2) Banking services for an existing account\n3) Exit\n")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            name = input("Please enter your name: ")
            user_input = input("Please enter your initial deposit amount: ")
            try:
                initial_balance = int(user_input) if user_input else 0
            except ValueError:
                print("Invalid amount. Starting with $0.")
                initial_balance = 0
            BankAccount(name, initial_balance)
            print("Account creation successful!")

        elif choice == 2:
            if not BankAccount.bank_accounts:
                print("No accounts found. Please create one first.")
                continue

            name = input("Enter your name: ")
            user_list = [acc for acc in BankAccount.bank_accounts if acc._BankAccount__account_holder_name == name]

            if not user_list:
                print("Account not found.")
                continue

            user = user_list[0]

            print("""
---------- Welcome to your bank account ----------
What would you like to do?
1) Deposit
2) Withdraw
3) Check Balance
""")
            try:
                service_choice = int(input("Enter your option: "))
                if service_choice == 1:
                    amount = int(input("Enter amount to deposit: "))
                    print(user.deposit(amount))
                elif service_choice == 2:
                    amount = int(input("Enter amount to withdraw: "))
                    print(user.withdraw(amount))
                elif service_choice == 3:
                    print(user.get_balance())
                else:
                    print("Invalid service option.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == 3:
            print("👋 Exiting... Thank you!")
            break
        else:
            print("Invalid main menu option. Try again.")

if __name__ == "__main__":
    main()
