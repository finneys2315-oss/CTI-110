# Savon Finney

# P4LAB2

#3/19/2026

# Creating our variable and while loops

question = ""

while question not in ["Yes", "y", "Y", "yes", "Yes Pls", "Of Course"]:
    
    #The logic of the loop goes here
    
    Number = int(input("Give me an integer: "))
    
    if Number >= 0:
        for x in range(1, 13):
            print(f"{Number} * {x} = {Number * x}")
    else:
        print("No negatives number pls")
    
    question = input("Do you want to end the program?: ")
    
    
    
    # Making sure the while loops can break
    

print("The program has ended")