# Savon Finney

# 3/3/2026

#P3Lab

# Working with branching functions and floor divisions.

import math

# Getting a float from the user.

user_change = float(input("Enter the amount of money with 2 decimal places:$"))

# Changing the float input from the user into a integer.

if user_change == 0.00:
    print("No change")

user_change = int(user_change * 100)

# print(f"Change = ${user_change}.")

# Determining the numbers dollars from change using floor division.


dollars = user_change // 100

# print(f"Dollar amount: ${dollars}.")

# Determining the quarter amount from using floor division.


quarter = user_change // 25


# print(f"Quarter amount = {quarter} ")

# Determining the dime amount from using floor division

dime = user_change // 10

# print(f"Dime amount = {dime}")

# Determining the nickel amount from using floor division.

nickel = user_change // 5

# print(f"Nickel amount = {nickel}")


# Determining the pennies amount from change using floor division.

pennies = user_change // 1

# print(f"Pennies = {pennies}")

# Only print coins that are you needed to display

if dollars > 0 :
    
    if dollars == 1:
    
        print(f"{dollars} dollar.")
    else:
        print(f"{dollars} dollars.")
    if quarter > 0:
        if quarter == 1:
            print(f"{quarter} quarter")
    else:
        print(f"{quarter} quarters.")
    if dime > 0:
        if dime == 1:
            print(f"{dime} dime.")
        
    else:
        print(f"{dime} dimes")
    if nickel > 0:
        if nickel == 1:
            print(f"{nickel}. nickel")
    else:
        print(f"{nickel}. nickels")
    if pennies > 0:
        if pennies == 1:
            print(f"{pennies}. penny")
    else:
        print(f"{pennies}. pennies")
        
        
        
        
        
        
        
        
        
    
    
    







