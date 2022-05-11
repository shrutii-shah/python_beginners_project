#Beginners madlib project - simple
#This project uses user input, string formatting and print statement
#The sample story copied from https://www.pinterest.com/pin/110127153364852209/ requires - 2 person,2 noun,4 verb and 6 adjective.

#Taking user input required for the story


print("\nYou can repeat person name, noun, verb and adjective as many times as you want.\n")
person1 = input("Enter the 1st person: ")
person2 = input("Enter the 2nd person: ")
noun1 = input("Enter the 1st noun: ")
noun2 = input("Enter the 2nd noun: ")
verb1 = input("Enter the 1st verb: ")
verb2 = input("Enter the 2nd verb: ")
verb3 = input("Enter the 3rd verb: ")
verb4 =input("Enter the 4th verb: ")
adjective1 = input("Enter the first adjective: ")
adjective2 = input("Enter the second adjective: ")
adjective3 = input("Enter the 3rd adjective: ")
adjective4 = input("Enter the fourth adjective: ")
adjective5 = input("Enter the 5th adjective: ")
adjective6 = input("Enter the 6th adjective: ")


madlib_story = (f"Yesterday, {person1} and I went to the park. On our way to the {adjective1}, we saw a {adjective2} {noun1} on a bike. " 
                f"We also saw big {adjective3} balloons tied to a {noun2}. Once we got to the {adjective4} park, the sky turned {adjective5}. "
                f"It started to {verb1} and {verb2}. {person2} and I {verb3} all the way home. Tomorrow we will try to go to the {adjective6} "
                f"park again and hope it doesn't {verb3}. ")

print(madlib_story)
