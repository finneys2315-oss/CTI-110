# Savon Finney

# 3/12/2026

# P3HW2_FinneySavon

# Creating a program that record employees worktime and calacute the their gross pay.


import math

# Geting our employee values from our user

employee_name = input("What is the employee name?: ")

employee_hours = float(input("How many hours did the employee work this week?: "))

employee_pay_rate = float(input("What is the employee pay rate?: "))


# Check to see if the employee in question has work overtime

if employee_hours > 40:
    overtime = employee_hours - 40
    
    RegHour_Pay =  employee_hours * employee_pay_rate
    
    OverTime_Pay = overtime * employee_pay_rate * 1.5
    
    Gross_Pay = OverTime_Pay + RegHour_Pay
else:
    RegHour_Pay = employee_hours * employee_pay_rate
    
    OverTime_Pay = 0
    
    Gross_Pay = RegHour_Pay + OverTime_Pay
    
    overtime = 0
    

# Displaying our results to the user

print("----------------------------------")

print(f"Employee name: {employee_name} ")
print("")
print(f"Hours Worked    Pay Rate        OverTime     OverTime Pay     RegHour Pay       Gross Pay")
print("-----------------------------------------------------------------------------------------------------")
print(f"{employee_hours}   {employee_pay_rate:>14}   {overtime:>12}  {OverTime_Pay:>12}    {RegHour_Pay:>15}   {Gross_Pay:>15} ")


