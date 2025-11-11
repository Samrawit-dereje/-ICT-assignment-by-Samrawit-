balance = 1000.000 
print(f"Your balance is $")
while True:  
    amount = float(input("Enter how much to withdraw : $"))

    if amount > balance:
        print("Not enough money.")
    else:
        balance -= amount
        print("You took out $", amount)
        print("Your new available balance is $", balance)
..: