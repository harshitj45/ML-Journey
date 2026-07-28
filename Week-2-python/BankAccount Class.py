# ============================================
# PROGRAM 25: BankAccount Class
# CONCEPTS: class, __init__, methods,
#           class variable, instance variable,
#           dunder methods, method chaining
# ============================================

class BankAccount:

    bank_name = "ML Bank"

    def __init__(self, owner, balance=0):
        self.owner   = owner
        self.balance = balance
        self.history = []       

    def deposit(self, amount):
 
        if amount <= 0:
            print("Amount should be positive !")
            return self
        self.balance += amount
        self.history.append(f"Deposit: +{amount}")
        return self         

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! Balance: {self.balance}")
            return self
        self.balance -= amount
        self.history.append(f"Withdraw: -{amount}")
        return self             

    def show_history(self):
        print(f"\n{self.owner} Owner's history:")
        for item in self.history:
            print(f"  {item}")

    def __str__(self):
        return f"Account[{self.owner}] Balance: Rs.{self.balance}"

    def __gt__(self, other):
        return self.balance > other.balance


# ── TESTS ──

acc1 = BankAccount("Harshit", 10000)
acc2 = BankAccount("Priya", 5000)

# Method chaining:
acc1.deposit(2000).deposit(1000).withdraw(500)

print(acc1)         
print(acc2)        

# Dunder test:
print(acc1 > acc2)  # True

# Class variable:
print(BankAccount.bank_name)   
print(acc1.bank_name)          

# History:
acc1.show_history()
