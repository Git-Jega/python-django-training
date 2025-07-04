import random

class bank_account:
  bank_accounts = []
  def __init__(self, name, balance = 0):
    self.__account_number = random.randint(10**11,(10**12)-1)
    self.__account_holder_name = name
    self.__balance = balance
    bank_account.bank_accounts.append(self)
  '''def __str__(self):
     return f"{self.__balance} is the balance for {self.__account_holder_name} with account number {self.__account_number}"'''
  def deposit(self):
    amount = int(input("Enter amount : "))
    self.__balance = self.__balance + amount
    return f"Successfully deposited {amount} to your account"
  def withdraw(self):
    amount = int(input("Enter amount : "))
    self.__balance = self.__balance - amount
    return f"Successfully withdrawed {amount} to your account"
  def get_balance(self):
    return f"${self.__balance}"

def main():
  while True:
    print("\n1) Create a new bank account\n2) Banking services for an existing account\n3) Exit\n")
    choice = int(input("Enter your choice : "))
    if choice == 1:
      name = input("Please enter your name : ")
      user_input = input("Please enter your initial deposit ammount : ") 
      initial_balance = int(user_input) if user_input else 0
      bank_account(name,initial_balance)
      print("\nAccount creation successful")
    elif choice == 2:
      if len(bank_account.bank_accounts)>0:
        name = input("\nPlease enter your name : ")
        user = [obj for obj in bank_account.bank_accounts if obj._bank_account__account_holder_name == name][0]
        print("""---------- Welcome to your bank account helper ----------
          What you want to do
        1)Deposit
        2)withdraw
        3)check balance""")
        options = {1: user.deposit,
                  2: user.withdraw,
                  3: user.get_balance}
        try:
          choice = int(input())
          action = options.get(choice)
          if action:
            print(action())
          else:
            print("Invalid choice")
        except ValueError:
          print("please enter a valid input")
      else:
        print("There are no accounts at the moment. Please create an account to use services")
        continue
    elif choice == 3:
      break


if __name__ == "__main__":
  main()
