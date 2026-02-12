# Savon Finney

# 02/12/2026

# P1HW2

# Making a travel budget for users.

# This is where calacute our expenses for our budget.

user_budget =  int(input("What is your budget?: "))
user_destination = input("What is your destination?: ")

user_expense = int(input("What is amount you will spend on gas?: ")) 
user_second_expense = int(input("What is the amount you will spend on accomodations?: "))
user_third_expense = int(input("What is the amount you will spend on food?: "))

user_total_expense = user_expense + user_second_expense + user_third_expense

user_budget_results = user_budget - user_total_expense

# Our Travel Budget


print()

print("Travel Budget")
print()
print(f"Your Budget:{user_budget}")
print()
print("Your expenses:")
print()
print(f"Gas amount: {user_expense}")
print()
print(f"Accomodations amount: {user_second_expense}")
print()
print(f"Food amount: {user_third_expense}")
print()
print()
print(f"Our remaining balance: {user_budget_results} ")

print()

print(type(user_budget))
print(type(user_expense))
print(type(user_second_expense))
print(type(user_third_expense))
