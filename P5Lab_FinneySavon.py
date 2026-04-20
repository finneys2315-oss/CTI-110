import random


def disperse_change(change):
    # Getting a float from the user.
    user_change = round(change * 100)
    print(f"Change owed as integer: ${user_change}")

    # Checking if no change is needed
    if user_change == 0:
        print("No change")

    # Calculating the number of dollars using floor division
    dollars = user_change // 100
    # Calculating the number of quarters
    quarter = user_change // 25
    # Calculating the number of dimes
    dime = user_change // 10
    # Calculating the number of nickels
    nickel = user_change // 5
    # Calculating the number of pennies
    pennies = user_change // 1

    # Only print coins that are needed
    if dollars > 0:
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
            print(f"{dime} dimes.")
    if nickel > 0:
        if nickel == 1:
            print(f"{nickel} nickel.")
        else:
            print(f"{nickel} nickels.")
    if pennies > 0:
        if pennies == 1:
            print(f"{pennies} penny.")
        else:
            print(f"{pennies} pennies.")


def main():
    # Fixing the typo for the amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owed: ${amount_owed:.2f}")
    money_in = float(input("How much cash do you want to put in cashout?: "))
    change = money_in - amount_owed
    print(f"Change owed: ${change:.2f}")

    # Passing the change to disperse_change function
    disperse_change(change)


main()        
        
        
        
        
    
    
    







