"""
File: hw3_part1.py
Author: Fey Alonge
Date: 9/24/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Greets customers coming into a cheese shop
 """

if __name__ == '__main__':
    cheese= input("Do you like cheese? ")
    if cheese == "No" or cheese == "no":
            print("Then why are you in a cheese shop?")
    elif cheese == "Yes" or cheese == "yes":
            cheddar = input("Is cheddar ok? ")
            if cheddar == "No" or cheddar == "no":
                print("Oh, I'll find you something else then.")
            elif cheddar == "Yes" or cheddar == "yes":
                print("Very well, here you are.")
            else:
                print("I don't know what you're talking about.")
    else:
            print("I don't know what you're talking about.")
