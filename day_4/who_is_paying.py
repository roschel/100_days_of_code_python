import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


# x = len(names)
# random_name = random.randint(0, x - 1)

print(f"{random.choice(names)} is going to pay the bill today")
