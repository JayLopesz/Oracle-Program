# imports random method to our code
import random as r

# It stores the name of the user in a variable
Traveller_Name = input(print("What's your name young traveller? "))

# It stores the question of the user in a variable
Traveller_Question = input(print("Make a [yes] or [no] question to the oracle, and you shall find your answer"))

# Stores a random number within a variable
oracle_answer = r.randint(1,9)
print(oracle_answer)

print(Traveller_Name + " Asks: " + Traveller_Question)

# if and elifs statements
if oracle_answer == 1:
    print("Yeah Sure")
elif oracle_answer == 2:
    print("I would not be so sure about that")
elif oracle_answer == 3:
    print("Definetly not")
elif oracle_answer == 4:
    print("Oh oh, you shall ask again")
elif oracle_answer == 5:
    print("I don't know for sure")
elif oracle_answer == 6:
    print("possibly yes")
elif oracle_answer == 7:
    print("That will depend on your efforts")
elif oracle_answer == 8:
    print("It's better for you not know")
elif oracle_answer == 9:
    print("My sources say yes")


