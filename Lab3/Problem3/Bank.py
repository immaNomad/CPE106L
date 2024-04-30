import pickle
import random
from savingsaccount import SavingsAccount

class Bank:
    def __init__(self, file_name=None):
        self.accounts = {}
        self.file_name = file_name
        if file_name:
            try:
                with open(file_name, 'rb') as file_obj:
                    while True:
                        try:
                            account = pickle.load(file_obj)
                            self.add(account)
                        except EOFError:
                            break
            except FileNotFoundError:
                pass

    def __str__(self):
        sorted_accounts = sorted(self.accounts.values(), key=lambda account: account.get_name())
        return "\n".join(map(str, sorted_accounts))

    def make_key(self, name, pin):
        return f"{name}/{pin}"

    def add(self, account):
        key = self.make_key(account.get_name(), account.get_pin())
        self.accounts[key] = account

    def remove(self, name, pin):
        key = self.make_key(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        key = self.make_key(name, pin)
        return self.accounts.get(key, None)

    def compute_interest(self):
        total_interest = 0
        for account in self.accounts.values():
            total_interest += account.compute_interest()
        return total_interest

    def save(self, file_name=None):
        if file_name:
            self.file_name = file_name
        elif self.file_name is None:
            return

        with open(self.file_name, 'wb') as file_obj:
            for account in self.accounts.values():
                pickle.dump(account, file_obj)

def create_bank(num_accounts=1):
    names = ("Brandon", "Molly", "Elena", "Mark", "Tricia", "Ken", "Jill", "Jack")
    bank = Bank()
    upper_pin = num_accounts + 1000
    for pin_number in range(1000, upper_pin):
        name = random.choice(names)
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pin_number), balance))
    return bank

def test_account():
    account = SavingsAccount("Ken", "1000", 500.00)
    print(account)
    print(account.deposit(100))
    print("Expect 600:", account.get_balance())
    print(account.deposit(-50))
    print("Expect 600:", account.get_balance())
    print(account.withdraw(100))
    print("Expect 500:", account.get_balance())
    print(account.withdraw(-50))
    print("Expect 500:", account.get_balance())
    print(account.withdraw(100000))
    print("Expect 500:", account.get_balance())

def main(number=10, file_name=None):
    test_account()
    if file_name:
        bank = Bank(file_name)
    else:
        bank = create_bank(number)
    print(bank)

if __name__ == "__main__":
    main()
