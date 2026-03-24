# Savon Finney 

# 3/24/2026

# P4HW1_FinneySavon

# Assignment assess student ability to edit and enhance exiting programs


# Asking the user for the amount of the scores they want.


user_score = int(input("What is the amount of scores you want to enter?: "))


vaild_score_list = []

vaild_score = 0

Done = ""

# Creating the loops for the amount of scores the user entered

for x in range(user_score):
    while Done not in ["Yes," "Done", "Finish"]:
        score = float(input("What is the score?: "))
        if 0 < score < 100:
            vaild_score_list.append(score)
        else:
            score = float(input("Invaild Score, pls input a score between 0 and 100: "))
        Done = input("Are you done?: ")

