# Step 1: Custom Exception Class
class InsufficientBalanceError(Exception):
    def __init__(self, balance, withdraw):
        self.message = f"Withdrawal of ₹{withdraw} failed. Available balance is only ₹{balance}."
        super().__init__(self.message)  # Call parent class constructor

# Step 2: Function to simulate withdrawal
def withdraw_money(balance, amount):
    if amount > balance:
        # Step 3: Raise custom exception
        raise InsufficientBalanceError(balance, amount)
    else:
        balance -= amount
        print(f"Withdrawal successful! Remaining balance: ₹{balance}")

# Step 4: Main Program with try-except
try:
    current_balance = 1000
    withdraw_amount = 1500
    withdraw_money(current_balance, withdraw_amount)

except InsufficientBalanceError as e:
    print(" Error:", e)
