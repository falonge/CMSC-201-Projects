"""
File: hw1_part6.py
Author: Fey Alonge
Date: /2019
Section: 201
E-mail: falonge1@umbc.edu
Description: Asks the user for information about a bill they’ve received, and calculates and prints out how much they should pay in total.
 """

bill = float(input("How much was the bill? "))
tax = float(input("How much is tax in your area? "))
tip = float(input("What percentage would you like to tip? "))
print("The total cost of the meal will be", bill+(bill*(tax/100))+(bill*(tip/100)))
