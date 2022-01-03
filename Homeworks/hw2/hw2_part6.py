"""
File: hw2_part6.py
Author: Fey Alonge
Date: 9/18/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Door access program
 """

first_lever = input("Do you pull the first lever? ")
second_lever = input("Do you pull the second lever? ")
third_lever = input("Do you pull the third lever? ")
if (first_lever == "yes" or third_lever == "yes") and second_lever == "no":
        print("The door opens!")
else:
        print("The door remains shut.")
        
