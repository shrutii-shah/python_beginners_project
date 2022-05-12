#Beginners Quiz Game - simple
#print statement
#User Input
#If Else statement

print("Welcome to the python Quiz game, answer the question and get your score")
player = input("\nDo you want to play? ").lower()

if player != "yes":
    quit()
print("Now the game will begin!!")
score = 0

quiz = input("Is python case-sensative?: ").lower()
if quiz == "yes":
    print("Correct Answer!!")
    score += 1
else:
    print("Incorrect Answer!!")

print(f"Your current score is {score}")


quiz = input("Django and Pyramid both are python framework, Yes or No?: ").lower()
if quiz == "yes":
    print("Correct Answer!!")
    score += 1
else:
    print("Incorrect Answer!!")
print(f"Your current score is {score} ")


quiz = input("Python is not used for building websites, Yes or No?: ").lower()
if quiz == "no":
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer!!")
print(f"Your current score is {score}")


quiz = input("Python is not an object oriented, Yes or No?: ").lower()
if quiz == "no":
    print("Correct!!")
    score +=1
else:
    print("Incorrect Answer!!")
print(f"Your current score is {score}")


quiz = input("There is a difference between Single and double quoted string in python, Yes or No: ").lower()
if quiz == "no":
    print("Correct!!")
    score += 1
else:
    print("Incorrect Answer!!")
print(f"Yout current score is {score}")

print(f"The game ends here!! \nYou got {score} questions correct so your percentage score is {(score/5)*100}% ")
