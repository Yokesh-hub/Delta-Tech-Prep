account_balance = 1000
def withdraw_pop(amount):
    global account_balance 
    if amount > account_balance:
        print("Error: Insufficient funds.")
    else:
        account_balance -= amount
        print(f"Successfully withdraw {amount}, New balance: {account_balance}")

print("       <Bank Account Details> ")
print(f"Initial balance: {account_balance}")
print("Accidentally changing the balance ")
account_balance = 10000
print(f"Balance after Accidental change: {account_balance}")
withdraw_pop(50) 

Output
<Bank Account Details> 
Initial balance: 1000
Accidentally changing the balance 
Balance after Accidental change: 10000
Successfully withdraw 50, New balance: 9950