# ============================================
# Day 12 - Program 33
# Topic: BankAccount with @property
# Concepts: @property, @setter, computed property,
#           private variable, validation
# ============================================


class BankAccount:

    bank_name = "ML Bank"           # class variable

    def __init__(self, owner, balance=0):
        self.owner    = owner
        self._balance = balance     # _ = private convention
        self._history = []          # transactions list

    @property
    def balance(self):
        # Getter — balance read karo
        return self._balance

    @balance.setter
    def balance(self, value):
        # Setter — negative balance rok do
        if value < 0:
            print("Balance negative nahi ho sakta!")
            return
        self._balance = value

    @property
    def status(self):
        # Computed property — balance ke basis pe
        if self._balance >= 10000:
            return "Premium"
        elif self._balance >= 1000:
            return "Regular"
        else:
            return "Low Balance"

    def deposit(self, amount):
        if amount <= 0:
            print("Amount positive hona chahiye!")
            return self
        self._balance += amount
        self._history.append(f"Deposit  : +{amount}")
        return self                 # method chaining

    def withdraw(self, amount):
        if amount > self._balance:
            print(f"Insufficient funds! Balance: {self._balance}")
            return self
        self._balance -= amount
        self._history.append(f"Withdraw : -{amount}")
        return self                 # method chaining

    def show_history(self):
        print(f"\n{self.owner} ki history:")
        for item in self._history:
            print(f"  {item}")

    def __str__(self):
        return (f"Account[{self.owner}] | "
                f"Balance: Rs.{self._balance} | "
                f"Status: {self.status}")


# --- TESTING ---

acc = BankAccount("Harshit", 15000)

# Getter:
print(acc.balance)          # 15000

# Computed property:
print(acc.status)           # Premium

# Setter — valid:
acc.balance = 500
print(acc.status)           # Low Balance

# Setter — invalid:
acc.balance = -100          # Balance negative nahi ho sakta!
print(acc.balance)          # 500 — change nahi hua

# Deposit + withdraw + chaining:
acc.deposit(5000).deposit(2000).withdraw(1000)

print(acc)                  # Balance: Rs.6500 | Status: Regular
acc.show_history()

# Class variable:
print(BankAccount.bank_name)    # ML Bank