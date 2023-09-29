class Bank:
    def __init__(self, IFSC_Code, bankname, branchname, loc):
        self.IFSC_Code = IFSC_Code
        self.bankname = bankname
        self.branchname = branchname
        self.loc = loc

class Customer:
    def __init__(self, CustomerID, custname, address, contactdetails):
        self.CustomerID = CustomerID
        self.custname = custname
        self.address = address
        self.contactdetails = contactdetails

class Account:
    def __init__(self, AccountID, customer, balance=0):
        self.AccountID = AccountID
        self.customer = customer
        self.balance = balance

    def getAccountInfo(self):
        print(f"Account ID: {self.AccountID}")
        print(f"Customer ID: {self.customer.CustomerID}")
        print(f"Customer Name: {self.customer.custname}")
        print(f"Customer Address: {self.customer.address}")
        print(f"Customer Contact Details: {self.customer.contactdetails}")
        print(f"Account Balance: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into the account.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from the account.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

class SavingsAccount(Account):
    def __init__(self, AccountID, customer, SMinBalance, balance=0):
        super().__init__(AccountID, customer, balance)
        self.SMinBalance = SMinBalance

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= self.SMinBalance:
            self.balance -= amount
            print(f"Withdrew {amount} from the account.")
        else:
            print("Invalid withdrawal amount or minimum balance violation.")

def create_account():
    IFSC_Code = input("Enter IFSC Code: ")
    bankname = input("Enter Bank Name: ")
    branchname = input("Enter Branch Name: ")
    loc = input("Enter Location: ")
    CustomerID = input("Enter Customer ID: ")
    custname = input("Enter Customer Name: ")
    address = input("Enter Customer Address: ")
    contactdetails = input("Enter Customer Contact Details: ")
    AccountID = input("Enter Account ID: ")
    SMinBalance = float(input("Enter Minimum Balance for Savings Account: "))

    customer = Customer(CustomerID, custname, address, contactdetails)

    account_type = input("Enter account type (Savings/Other): ").lower()

    if account_type == "savings":
        account = SavingsAccount(AccountID, customer, SMinBalance)
    else:
        account = Account(AccountID, customer)

    return account

def perform_transaction(account):
    while True:
        print("\nTransaction Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Get Account Information")
        print("5. Go Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Account Balance: {account.balance}")
        elif choice == "4":
            account.getAccountInfo()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    while True:
        print("\nBank Application Menu:")
        print("1. Create New Account")
        print("2. Perform Transaction")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account = create_account()
        elif choice == "2":
            if 'account' not in locals():
                print("Please create an account first.")
            else:
                perform_transaction(account)
        elif choice == "3":
            print("Exiting Bank Application.")
            break
        else:
            print("Invalid choice. Please select again.")
