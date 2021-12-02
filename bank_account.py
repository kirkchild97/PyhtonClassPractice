class BankAccount:
    bank_name = "Bank of Murica"
    account_name = ""
    int_rate = 0
    bank_balance = 0

    accounts = []
    
    def __init__(self, account_name, int_rate, balance) -> None:
        self.account_name = account_name
        self.int_rate = int_rate
        self.bank_balance = balance
        BankAccount.accounts += [self]
        

    def deposit(self, amount):
        self.bank_balance += amount
        return self

    def withdraw(self, amount):
        self.bank_balance -= amount
        return self

    def display_account_info(self):
        print(f'''Bank Name: {self.bank_name}
        User: {self.account_name}
        Interest Rate: {self.int_rate}
        Balance: {self.bank_balance}
        ''')
        return self

    def yield_interest(self):
        self.bank_balance *= self.int_rate
        return self

    @classmethod
    def displayAccounts(cls):
        for account in BankAccount.accounts:
            account.display_account_info()


Kirkland = BankAccount("Kirkland", .05, 150)
Robert = BankAccount("Robert", .02, 2000)
Billy = BankAccount("Billy", .03, 2001)


Kirkland.deposit(100).deposit(200).deposit(255).withdraw(500).yield_interest().display_account_info()
Robert.deposit(500).deposit(250).withdraw(100).withdraw(5).withdraw(50).withdraw(500).yield_interest().display_account_info()
print("-------------------")
BankAccount.displayAccounts()