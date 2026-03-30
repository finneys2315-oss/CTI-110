# Savon Finney

# 3/29/2026

# P4HW2_FinneySavon

# Creating a program that record employees worktime and calacute the their gross pay.


import math

# Geting our employee values from our user

Done = ""
number_of_employees = 0

while Done not in ["Yes", "Done", "y", "Finished", "Y", "yes"]:

    employee_name = input("What is the employee name?: ")

    employee_hours = float(input("How many hours did the employee work this week?: "))

    employee_pay_rate = float(input("What is the employee pay rate?: "))
    # Check to see if the employee in question has work overtime
    if employee_hours > 40:
        overtime = employee_hours - 40
    
        RegHour_Pay =  employee_hours * employee_pay_rate
    
        OverTime_Pay = 40 * employee_pay_rate * 1.5
    
        Gross_Pay = OverTime_Pay + RegHour_Pay
    else:
        RegHour_Pay = employee_hours * employee_pay_rate
    
        OverTime_Pay = 0
    
        Gross_Pay = RegHour_Pay + OverTime_Pay
    
        overtime = 0
    number_of_employees = number_of_employees + 1

    Sum_of_hours = employee_hours + overtime * number_of_employees
    
    Total_Regular_pay = RegHour_Pay * number_of_employees
    Total_overtime_pay = OverTime_Pay * number_of_employees
    Total_Gross_pay = Total_Regular_pay + Total_overtime_pay
     #  Displaying our results to the user


    print("----------------------------------")

    print(f"Employee name: {employee_name} ")
    print("")
    print(f"Hours Worked    Pay Rate        OverTime     OverTime Pay     RegHour Pay       Gross Pay")
    print("-----------------------------------------------------------------------------------------------------")
    print(f"{employee_hours}   {employee_pay_rate:>14}   {overtime:>12}  {OverTime_Pay:>12}    {RegHour_Pay:>15}   {Gross_Pay:>15} ")
    print("")
    print("")
    Done = input("Would like you like to add another employee or are you done?: ")
print("")
print(f"Total number of employees entered: {number_of_employees:>5}")
print(f"Total amount paid for regular hours: ${Total_Regular_pay:>6.2f}")
print(f"Total amount paid for overtime hours: ${Total_overtime_pay:>4.2f}")
print(f"Total amount paid in gross: {'$':>11}{Total_Gross_pay:>1.2f}")




