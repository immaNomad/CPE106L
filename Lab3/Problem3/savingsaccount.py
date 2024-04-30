class SavingsAccount:
 
    # RATE (float): The annual interest rate for all accounts.

    RATE = 0.02

    def __init__(self, name: str, pin: str, balance: float = 0.0):
        """
        Initializes a new SavingsAccount instance.

        Args:
            name (str): The owner's name.
            pin (str): The account's PIN.
            balance (float, optional): The initial balance. Defaults to 0.0.
        """
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self) -> str:

        # Returns: str: A string containing the account owner's name, PIN, and balance.
        return f"Name: {self.name}\nPIN: {self.pin}\nBalance: {self.balance:.2f}"

    def get_balance(self) -> float:
 
        # Returns: float: The current balance.
        return self.balance

    def get_name(self) -> str:

        # Returns: str: The account owner's name.
        return self.name

    def get_pin(self) -> str:

        # Returns:str: The account's PIN.
        return self.pin

    def deposit(self, amount: float) -> str:
        """
        Adds the specified amount to the account balance.

        Args:
            amount (float): The amount to be deposited.

        Returns:
            str: An error message if the amount is invalid, otherwise None.
        """
        if amount < 0:
            return "Amount must be greater than or equal to 0."
        self.balance += amount
        return None

    def withdraw(self, amount: float) -> str:
        """
        Subtracts the specified amount from the account balance.

        Args:
            amount (float): The amount to be withdrawn.

        Returns:
            str: An error message if the amount is invalid or the balance is insufficient, otherwise None.
        """
        if amount < 0:
            return "Amount must be greater than or equal to 0."
        if self.balance < amount:
            return "Insufficient funds."
        self.balance -= amount
        return None

    def compute_interest(self) -> float:
        """
        Computes, deposits, and returns the interest earned on the account balance.

        Returns:
            float: The interest earned.
        """
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest