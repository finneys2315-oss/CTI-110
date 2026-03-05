# Savon Finney

# 3/5/2026

# P3HW1

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

import math

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_1 = float(input('Enter grade for Module 5: '))
mod_5 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = math.fsum(grades)
avg = high / 5

# determine letter grade for average


# Display the user grades

print('---------------Results-----------')

print(f"Lowest Grade: {low}")
print(f"Highest Grade: {high}")
print(f"Sum of Grades: {sum}")
print(f"Average: {avg}")

print(f"-----------------------------------")

if avg >= 90:
    print('Your grade is: A')
else:
    if avg >= 80:
        print('Your grade is: B')
if avg >= 70:
    print('Your grade is: C')
else:
    if avg >= 50:
        print('Your grade is: D')
    else:
        if avg >= 30:
            print('Your grade is F')












