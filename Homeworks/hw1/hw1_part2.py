"""
File: hw1_part2.py 
Author: Fey Alonge
Date: /2019
Section: 201
E-mail: falonge1@umbc.edu
Description: Asks the user how much money they make, the cost of their favorite candy bar, and calculates how many candy bars they earned that day
 """

income = float(input("How much money do you make in a day?"))
candy_bar_cost = float(input("How much does your favorite candy bar cost?"))
print("You earned", income / candy_bar_cost, "candy bars today!")
