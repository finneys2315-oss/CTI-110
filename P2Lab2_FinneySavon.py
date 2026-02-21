# Savon Finney

# 02/19/2026

# P2Lab2

# Learning how to use dictionary in Python.

family_of_values = {'Camro':18.21, 'Prius':52.36, "Model S":110, "Silverado":26}

car_keys = family_of_values.keys()

print(f"Here is our list of cars:{car_keys}")
print()


choose_your_car = input("Which car you want to ride?: ")
print()

print(f"{choose_your_car} has {family_of_values[choose_your_car]}")

print()

Miles = float(input(f"How manys miles you want to drive {choose_your_car}?: "))
print()


Gallons = Miles * 0.02

print(f"{Gallons} gallons of gas are needed to drive {choose_your_car} {Miles} miles.")

