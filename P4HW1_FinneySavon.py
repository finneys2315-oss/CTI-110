# Savon Finney 

# 3/24/2026

# P4HW1_FinneySavon

# Assignment assess student ability to edit and enhance exiting programs


# Asking the user for the amount of the scores they want.

import math


user_score = int(input("What is the amount of scores you want to enter?: "))




vaild_score_list = []

vaild_score = 1

Done = ""

# Creating the loops for the amount of scores the user entered
while Done not in ["Yes", "Y","yes", "y" "Done", "Finish"]:
    for x in range(user_score):
        
        score = float(input(f"Enter score {vaild_score}: "))
        
        if -1 < score < 101:
            vaild_score_list.append(score)
            vaild_score = vaild_score + 1
        else:
            print("INVAILD SCORE ENTERED!!!!!!!!!!!!, score should be between 0 and 100")
            score = float(input(f"Enter score {vaild_score} again: "))
            vaild_score = vaild_score + 1
    Done = input("Are you done?: ")        

Low = min(vaild_score_list)
High = max(vaild_score_list)
sum = math.fsum(vaild_score_list)
average = sum / user_score
Grade = ""
if average == 100:
    Grade = "A+"
else:
    if average >= 90 < 100:
        Grade = "A"
    else:
        if average >= 70 < 90:
            Grade = "B"
        else:
            if average >= 50 < 70:
                Grade = "C"
            else:
                if average >= 40 < 50:
                    Grade = "D"
                else:
                    if average < 40:
                        Grade = "F"





# Display our the score our user inputted

print("---------------Results-------------------")

print(f"{'Lowest Score'} : {Low:>6}")
print(f"{'Modified List'} : {vaild_score_list}")
print(f"{'Scores Average'} : {average:>5.2f}")
print(f"{'Grade'}      : {Grade:>5}")

print("----------------Results------------------")


print("The program has ended")