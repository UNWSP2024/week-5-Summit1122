# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
import random


def number_adder(n1, n2):
     result1 = n1 + n2
     return result1

randomN1 = random.randint(100, 800)
randomN2= random.randint(100,800)
result = number_adder(randomN1, randomN2)

def users_answer():
    if user_A == result:
        print("That is Correct! :)")
    else:
        print("Sorry that is incorrect :[")


print(f"What is {randomN1} + {randomN2}?")
user_A = int(input("Enter answer here: "))
users_answer()