"""
File: major.py
Author: Fey Alonge
Date: 9/19/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Asks the user what their major is and tells them the grade they'll need to pass
 """

major = input("Please enter your major: ")
if major == "CMSC" or major == "CMPE":
        print("You need to earn at least a B for CMSC 201 to count")
else:
        print("You need to earn at least a C for CMSC 201 to count")
