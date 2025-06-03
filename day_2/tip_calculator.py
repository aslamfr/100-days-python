bill_i = float(input("What was the total bill? ($) "))
tip_i = int(input ("How much tip (%) would you like to give? "))
split = int(input("How many people to split the bill? "))

tip = (bill_i * tip_i)/100
bill = bill_i + tip
pay = bill/split

print(f"Each person should pay: ${round(pay, 2)}")