# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
total_tip_percentage = float(input("What percentage tip would you like to give? "))
total_people = int(input("How many people to split the bill? "))

total_bill_with_tip = total_bill * (1 + total_tip_percentage / 100)
total_bill_per_person = total_bill_with_tip / total_people

print(f"Each person shpuld pay: ${round(total_bill_per_person, 2)}")
