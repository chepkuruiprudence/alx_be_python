class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional initial balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a positive amount to the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw if sufficient funds are available. Returns True/False."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
