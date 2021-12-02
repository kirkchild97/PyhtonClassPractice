from bank_account import BankAccount


class User:
    user_name = ""
    user_accounts = {}

    def __init__(self, user_name, account_name = "Checking", int_rate = .01, starting_amount = 0) -> None:
        self.user_name = user_name
        self.funds_amount = starting_amount
        self.user_accounts[account_name] = BankAccount(account_name, int_rate, starting_amount)

    def make_new_account(self, account_name, int_rate, amount = 0):
        self.user_accounts[account_name] = BankAccount(account_name, int_rate, amount)
        return self

    def make_deposit(self, account_name, amount):
        self.user_accounts[account_name].deposit(amount)
        return self
    
    def make_withdrawal(self, account_name, amount):
        self.user_accounts[account_name].withdraw(amount)
        return self

    def display_all_user_balance(self):#display all account balances
        for account in self.user_accounts:
            print(account)
            self.user_accounts[account].display_account_info()
        return self
    def display_user_balance(self, account_name):#display single account balance
        self.user_accounts[account_name].display_account_info()
        pass

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_withdrawal(-amount)
        return self

Jessica = User("Jessica", starting_amount=12000)
Jessica.make_deposit("Checking", 500).make_new_account("Savings", .05, 5000).display_all_user_balance()