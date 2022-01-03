"""
File: hw4_part4.py
Author: Fey Alonge
Date: 10/1/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Mushroom record keeper
 """

if __name__ == "__main__":
    mushroom_list = [] #empty string to hold mushrooms
    # integers to keep track of large, medium, and small mushrooms
    large = 0
    medium = 0
    small = 0
    mushroom = int(input("Enter a mushroom weight, or STOP to end. "))
    if mushroom <= 0:
            print("Weights must be greater than 0!")
    elif mushroom > 1000:
            large += 1
    elif mushroom < 100:
            small += 1
    else:
            medium += 1

    while mushroom != "STOP":
        if mushroom > 0:
            mushroom_list.append(mushroom)
        mushroom = input("Enter a mushroom weight, or STOP to end. ")
        # prevents the program from throwing an error if the user enters STOP
        if mushroom != "STOP":
            mushroom = int(mushroom)
            if mushroom <= 0:
                print("Weights must be greater than 0!")
            elif mushroom > 1000:
                large += 1
            elif mushroom < 100:
                small += 1
            else:
                medium += 1
    print("The weights you entered were", mushroom_list)
    print("There were", large, "large mushrooms,", medium, "mediums, and", small, "smalls. ")
