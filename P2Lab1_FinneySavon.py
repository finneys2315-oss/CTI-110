# Savon Finney

# 2/17/2026

# P2Lab1 Instructions

# Learning how to write code that performs mathematical calculations and display that information for users.

# Our cicrle formula

import math

# print(math.pi)


radius = float(input("What is the radius of the circle?: "))

diameter = 2 * radius

circumference = 2 * math.pi * radius

area = math.pi * math.pow(radius, 2)

# Here we print out the results to the user

print()

print(f"The diameter of the circle is {diameter:.1f}")

print()

print(f"The circumference of the circle is {circumference:.2f}")

print()

print(f"The area of the circle is {area:.3f}.")

print()