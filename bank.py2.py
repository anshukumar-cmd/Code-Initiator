class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance


class BalanceInquiry(BankAccount):
    def show_balance(self):
        print("Account No:", self.acc_no)
        print("Name:", self.name)
        print("Balance:", self.balance)


class Deposit(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("New Balance:", self.balance)


class Withdrawal(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Remaining Balance:", self.balance)
        else:
            print("Aukat nahi hai teri....")


# Object for Balance Inquiry
b1 = BalanceInquiry(101, "Rahul", 5000)
print("Balance Inquiry")
b1.show_balance()

# Object for Deposit
d1 = Deposit(102, "Aman", 7000)
print("\nDeposit")
d1.deposit(2000)

# Object for Withdrawal
w1 = Withdrawal(103, "Rohan", 6000)
print("\nWithdrawal")
w1.withdraw(150000)