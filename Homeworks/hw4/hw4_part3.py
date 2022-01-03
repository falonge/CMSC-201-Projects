"""
File: hw4_part3.py
Author: Fey Alonge
Date: 10/1/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Clothing design requests
 """

if __name__ == "__main__":
    design = input("Hello customer! What kind of design are you looking for? Valid options are 'classy', 'playful', or 'business'")
    while design != "classy" and design !="playful" and design != "business":
        print(design, "is not a valid style.")
        design = input("What kind of design are you looking for? Valid options are 'classy', 'playful', or 'business'")

    MINIMUM_TIME = 7
    time = int(input("How many days from now do you need the design? (Our minimum wait time is one week)"))
    while time < MINIMUM_TIME:
        print("Sorry, we need at least a week for the design.")
        time = int(input("How many days from now do you need the design? (Our minimum wait time is one week)"))

    MINIMUM_HEIGHT = 0
    height = int(input("What is your height in inches? "))
    while height <= MINIMUM_HEIGHT:
        print("Height must be greater than 0.")
        height = int(input("What is your height in inches? "))

    print("Great! We will get to work on a", design, "for a", height, "inch tall human. It will be ready in", time, "days or less.")
