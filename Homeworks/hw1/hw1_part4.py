"""
File: hw1_part4.py
Author: Fey Alonge
Date: 9/10/2019
Section: 201
E-mail: falonge1@umbc.edu
Description: Asks the user for information about an aircraft they own, and calculates the annual cost of owning it.
 """

inspections = float(input("What was the cost of annual inspections? "))
fuel = float(input("What was the cost of the fuel? "))
hangar = float(input("What was the cost of the hangar fees? "))
propeller = float(input("What was the cost of the cost of the propeller fluid? "))
print("The total annual cost of the aircraft is", inspections + fuel + hangar + propeller)
