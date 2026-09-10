import csv
from datetime import datetime
class BankAccount:
    bank_name = "Python National Bank"
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance = self._balance + amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
            return False
        else:
            self._balance = self._balance - amount
            return True

    def check_balance(self):
        if isinstance(self, SavingsAccount):
            account_type = "savings account"
        else:
            account_type = "regular account"

        print(f"{self.owner}'s {account_type} balance is: ${self._balance}")


    def transfer(self, other_account, amount):
        if amount > self._balance:
            print("Insufficient funds for transfer")
            return False
        else:
            self._balance = self._balance - amount
            other_account._balance = other_account._balance + amount
            return True

    def __str__(self):
        return f"{self.owner}'s account - Balance: ${self._balance}"

class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self._balance * 0.05
        self.deposit(interest)

    def __str__(self):
        return f"{self.owner}'s savings account - Balance: ${self._balance}"


accounts = {}
def save_accounts():
    with open("accounts.csv", "w") as file:
        writer = csv.writer(file)
        for owner, account in accounts.items():
            if isinstance(account, SavingsAccount): 
                account_type = "savings"
            else: 
                account_type = "regular"

            writer.writerow([account.owner, account._balance, account_type])

def load_accounts():
    try:
        with open("accounts.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                owner, balance, account_type = row
                balance = float(balance)
                account_key = owner + "-" + account_type
                if account_type == "savings":
                    accounts[account_key] = SavingsAccount(owner, balance)
                else:
                    accounts[account_key] = BankAccount(owner, balance)
    except FileNotFoundError:
        pass

load_accounts()
choice = ""

while choice != "quit":

    print("1.Create a new account")
    print("2.Deposit money")
    print("3.Withdraw money")
    print("4.Check balance")
    print("5.Transfer money")
    print("6.Add interest to savings account")
    print("7.Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        owner = input("Enter your account name: ")
        starting_balance = float(input("Enter your starting balance: "))
        account_type = input("Enter 'savings' for a savings account, or press Enter for a regular account:")
        account_key = owner + "-" + account_type.lower()
        if account_type.lower() == "savings":
            accounts[account_key] = SavingsAccount(owner, starting_balance)
        else:
            accounts[account_key] = BankAccount(owner, starting_balance)

        print("Your Account have been created successfully")
        save_accounts()

    elif choice == "2":
        owner_name = input("Enter your Name: ")
        account_type_request = input("Enter your account type (savings/regular): ")
        account_key = owner_name + "-" + account_type_request.lower()
        if account_key in accounts:
            deposit_amount = float(input("Enter the deposit amount: "))
            accounts[account_key].deposit(deposit_amount)
            print(f"You have  dposited ${deposit_amount} to {account_key}")
            save_accounts()
        else:
            print("Account not found")
        
    elif choice == "3":
        owner_name = input("Enter your Name: ")
        account_type_request = input("Enter your account type (savings/regular): ")
        account_key = owner_name + "-" + account_type_request.lower()
        if account_key in accounts:
            withdraw_amount = float(input("Enter withdrawwal amount: "))
            success = accounts[account_key].withdraw(withdraw_amount)
            if success:
                current_time = datetime.now()
                print(f"You have withdraw ${withdraw_amount} from your account at {current_time}.\nYour new balance is ${accounts[account_key]._balance}")
                save_accounts()
        else:
            print("Account not founds")

    elif choice == "4":
        owner_name = input("Enter your account name: ")
        account_type_request = input("Which account type do you want to access? (savings/regular): ")
        account_key = owner_name + "-" + account_type_request.lower()
        if account_key in accounts:
            accounts[account_key].check_balance()
        else:
            print("Account not found")

    elif choice == "5":
        sender_name = input("Enter sender's Name: ")
        sender_type = input("Enter sender type (savings/regular): ")
        sender_key = sender_name + "-" + sender_type.lower()
        receiver_name = input("Enter receiver's Name: ")
        receiver_type = input("Enter receiver type (savings/regular): ")
        receiver_key = receiver_name + "-" + receiver_type.lower()
        if sender_key in accounts and receiver_key in accounts:
            transfer_amount = float(input("Enter the transfer amount: "))
            confirm = input(f"Are you sure you want to send ${transfer_amount} to {receiver_name}? (yes/no)")
            if confirm.lower() == "yes":
                success = accounts[sender_key].transfer(accounts[receiver_key], transfer_amount)
                if success:
                    current_time = datetime.now()
                    print(f"You have transfer ${transfer_amount} to {receiver_key} at {current_time}.\nYour new balance is ${accounts[sender_key]._balance}")
                    save_accounts()
            else:
                print("Transfer cancelled")
        else:
            print("One or both accounts weren't found: ")


    elif choice == "6":
        owner_name = input("Enter your Name: ")
        account_key = owner_name + "-savings"
        if account_key in accounts:
            accounts[account_key].add_interest()
            save_accounts()
            print(f"Interest have been added to {account_key} successfully.")
        else:
            print("No savings account found for that name")

    





   

            



