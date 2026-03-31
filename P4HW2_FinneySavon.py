import math

Done = ""
number_of_employees = 0

total_hours = 0
total_regular_pay = 0
total_overtime_pay = 0
total_gross_pay = 0

while Done not in ["Yes", "DONE", "done", "Done", "y", "Finished", "Y", "yes"]:

    employee_name = input("What is the employee name?: ")
    employee_hours = float(input("How many hours did the employee work this week?: "))
    employee_pay_rate = float(input("What is the employee pay rate?: "))

    if employee_hours > 40:
        overtime = employee_hours - 40
        RegHour_Pay = 40 * employee_pay_rate
        OverTime_Pay = overtime * employee_pay_rate * 1.5
    else:
        overtime = 0
        RegHour_Pay = employee_hours * employee_pay_rate
        OverTime_Pay = 0

    Gross_Pay = RegHour_Pay + OverTime_Pay

    number_of_employees += 1

    # Add to totals
    total_hours += employee_hours
    total_regular_pay += RegHour_Pay
    total_overtime_pay += OverTime_Pay
    total_gross_pay += Gross_Pay

    print("----------------------------------")
    print(f"Employee name: {employee_name}")
    print("")
    print("Hours Worked    Pay Rate    OverTime    OT Pay    Reg Pay    Gross Pay")
    print("--------------------------------------------------------------------------")
    print(f"{employee_hours:<15}{employee_pay_rate:<12}{overtime:<12}{OverTime_Pay:<10.2f}{RegHour_Pay:<12.2f}{Gross_Pay:<10.2f}")

    Done = input("Add another employee or type 'Done' to terminate: ")

print("")
print(f"Total number of employees entered: {number_of_employees}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid for overtime hours: ${total_overtime_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")




