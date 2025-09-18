class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def get_balance(self):
        return self.__balance

    def withdraw_oop(self, amount):
        if amount > self.__balance:
            print("Error: Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Successfully withdraw {amount}, New balance: {self.__balance}")
print("    <Bank Account Details> ")
my_account = BankAccount(1000)
print(f"Initial balance: {my_account.get_balance()}")
print("Accidentally changing the balance")
try:
    my_account.__balance =5000000
except AttributeError as e:
    print(f"Error caught: {e}")

my_account.withdraw_oop(50)
print(f"Final balance: {my_account.get_balance()}")

Output
    <Bank Account Details> 
Initial balance: 1000
Accidentally changing the balance
Successfully withdraw 50, New balance: 950
Final balance: 950