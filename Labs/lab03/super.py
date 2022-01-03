"""
File: super.py
Author: Fey Alonge
Date: 9/19/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Asks the user if they are a hero or villain, and responds to information given
 """

villain_or_hero = input("Are you a hero or a villain? ")
if villain_or_hero == "villain":
        print(input("What is your name? "), "sounds pretty evil!!")
elif villain_or_hero == "hero":
        saved = int(input("How many people have you saved? "))
        if saved <= 10:
            print("Go on more patrols!")
        elif saved > 10 and saved < 100:
            print("Sounds like you're making a difference!")
        elif saved >= 100:
            print("Wow, great job saving the city!")
