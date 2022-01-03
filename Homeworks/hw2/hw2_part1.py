"""
File: hw2_part1.py
Author: Fey Alonge
Date: 9/18/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Prompts the user for the type of fish that they want to buy, and then gives them an answer that depends on the type of fish.
 """

fish_type = input("What type of fish would you like to purchase? ")
if fish_type == "carnivorous":
        carnivorous = input("Do you have smaller fish already? ")
        if carnivorous == "no":
                print("Great! Enjoy!")
        elif carnivorous == "yes":
                print("This is a bad idea! It\'ll eat your little ones!")
elif fish_type == "salt water":
    print("Wow, you\'re a fancy fish parent!")
elif fish_type == "community":
    community = int(input("How many fish of this species do you already have? "))
    if community < 3:
        print("You should get more than one!")
    else:
        print("Yay, more friends!")
else:
    print("I don\'t think that\'s a type of fish. Maybe you\'re looking for a lizard?")
