"""
Day 34 — Encapsulation & Properties
Problem: Create a class BankAccount with:

Private attribute __balance (starts at 0).
deposit(amount) — validates amount > 0.
withdraw(amount) — validates against balance and amount > 0.
@property balance — returns the current balance.
@balance.setter — prevents direct invalid setting.
transaction_history — list of all transactions with type and amount.
show_history() — prints the full transaction log.
Concepts: Encapsulation, name mangling, @property, @setter
"""

class BankAccount:
    def __init__(self):
        # Private attribute with name mangling (starts with __)
        self.__balance = 0.0
        # List to keep track of all transactions
        self.transaction_history = []

    @property
    def balance(self):
        """Getter method to view the balance securely."""
        return self.__balance

    @balance.setter
    def balance(self, value):
        """Setter method to prevent direct, unauthorized modification."""
        print("Error: Direct modification of balance is not allowed. Use deposit() or withdraw().")

    def deposit(self, amount):
        """Validates and deposits a positive amount into the account."""
        if amount > 0:
            self.__balance += amount
            self.transaction_history.append({"type": "Deposit", "amount": amount})
            print(f"Successfully deposited: ${amount:.2f}")
        else:
            print("Error: Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        """Validates amount and available balance before withdrawing."""
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than 0.")
        elif amount > self.__balance:
            print(f"Error: Insufficient funds. Current balance is ${self.__balance:.2f}")
        else:
            self.__balance -= amount
            self.transaction_history.append({"type": "Withdrawal", "amount": amount})
            print(f"Successfully withdrew: ${amount:.2f}")

    def show_history(self):
        """Prints the full transaction log."""
        print("\n--- Transaction History ---")
        if not self.transaction_history:
            print("No transactions recorded yet.")
        else:
            for idx, tx in enumerate(self.transaction_history, 1):
                print(f"{idx}. {tx['type']}: ${tx['amount']:.2f}")
        print(f"Current Balance: ${self.balance:.2f}\n")


# --- Example Usage & Verification ---
if __name__ == "__main__":
    account = BankAccount()

    # 1. Test initial balance and direct modification prevention
    print(f"Initial Balance: ${account.balance}")
    account.balance = 5000  # Attempts direct setting; triggers @balance.setter

    # 2. Test valid and invalid deposits
    account.deposit(-50)   # Invalid
    account.deposit(100.50) # Valid

    # 3. Test valid and invalid withdrawals
    account.withdraw(150)  # Invalid (Insufficient funds)
    account.withdraw(-10)  # Invalid (Negative amount)
    account.withdraw(40.25) # Valid

    # 4. Show the complete history
    account.show_history()

    # 5. Proof of Name Mangling
    # Attempting to access account.__balance directly will raise an AttributeError
    try:
        print(account.__balance)
    except AttributeError:
        print("Verified: Direct access to account.__balance is blocked via Name Mangling.")
