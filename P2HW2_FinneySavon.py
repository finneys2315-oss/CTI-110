# Savon Finney

# 2/26/2026

# P2HW2

# Learning and using lists in Python.


# Asking the users grade scores.

import math


Module_1 = float(input("What is your score for Module 1?: "))
Module_2 = float(input("What is your score for Module 2?: "))
Module_3 = float(input("What is your score for Module 3?: "))
Module_4 = float(input("What is your score for Module 4?: "))
Module_5 = float(input("What is your score for Module 5?: "))
Module_6 = float(input("What is your score for Module 6?: "))

# Storing the user scores in a list

Grades_for_our_user = [Module_1, Module_2, Module_3, Module_4, Module_5, Module_6]


# Displaying the grade results from our user's scores.


print(f"------Results------")
print()

print(f"Lowest Grade: {min(Grades_for_our_user)}")
print(f"Highest Grade: {max(Grades_for_our_user)}")
print(f"Sum of Grades: {math.fsum(Grades_for_our_user)}")




