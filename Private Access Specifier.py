class BankAccount:
    
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def get_balance(self):  
        return self.__balance

account1 = BankAccount("12345", 1000)

try:
    print(account1.__balance)
except AttributeError as e:
    print(f"Error caught: {e}") 
print(f"Current balance: {account1.get_balance()}") 

account1.deposit(500) 

Output:
Error caught: 'BankAccount' object has no attribute '__balance'
Current balance: 1000
Deposited: 500. New balance: 1500