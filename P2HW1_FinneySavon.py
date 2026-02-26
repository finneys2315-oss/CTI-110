# Savon Finney

# 2/26/2026


# P2HW1

# Learning how to edit and enhance exiting programs.


user_budget =  float(input("What is your budget?: "))
user_destination = input("What is your destination?: ")

user_expense = float(input("What is amount you will spend on gas?: ")) 
user_second_expense = float(input("What is the amount you will spend on accomodations?: "))
user_third_expense = float(input("What is the amount you will spend on food?: "))

dollar_sign = "$"

user_total_expense = user_expense + user_second_expense + user_third_expense

user_budget_results = user_budget - user_total_expense



# Our Travel Budget


print()

print("---------Travel Budget----------")
print()
print(f"Location: {user_destination:>18}")
print(f"Initial Budget: {dollar_sign:>7}{user_budget:.2f}")
print(f"Gas: {dollar_sign:>18}{user_expense:.2f}")
print(f"Accomodations: {dollar_sign:>8}{user_second_expense:.2f}")
print(f"Food: {dollar_sign:>17}{user_third_expense:>.2f}")
print(f"------------------------------")
print(f"Our remaining balance: ${user_budget_results:7.2f}")

print()

print(type(user_budget))
print(type(user_expense))
print(type(user_second_expense))
print(type(user_third_expense))

print()

print(type(user_budget))
print(type(user_expense))
print(type(user_second_expense))
print(type(user_third_expense))


