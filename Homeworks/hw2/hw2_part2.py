"""
File: hw2_part2.py
Author: Fey Alonge
Date: 9/18/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Ask the user to enter an integer and if they would like to know if that number is even, for it to be squared, or for it to be multiplied with another number. The user will input "even" "square" or "multiply" for these options, respectively.

 """

integer = int(input("Enter an integer: "))
answer = input("Would you like to know if this number is even, square it, or multiply it with another number? ")
if answer == "even":
        if (integer % 2) == 0:
                    print("It is even!")
        else:
                    print("It is odd!")
elif answer == "square":
        print("The square if this number is:", integer**2)
elif answer == "multiply":
        other_number = int(input("What is the other number? "))
        print(integer, "times", other_number, "is", integer * other_number)
else:
        print("I don\'t know what you\'re talking about")
