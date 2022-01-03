"""
File: hw2_part4.py
Author: Fey Alonge
Date: 9/18/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Day of the week calculator
 """

date = int(input("What day of September 2019 are we in? "))
if date < 1 or date > 30:
        print("That's not a valid day.")
elif (date % 7) == 1:
        print("It's Sunday")
elif (date % 7) == 2:
        print("It's Monday")
elif (date % 7) == 3:
        print("It's Tuesday")
elif (date % 7) == 4:
        print("It's Wednesday")
elif (date % 7) == 5:
        print("It's Thursday")
elif (date % 7) == 6:
        print("It's Friday")
elif (date % 7) == 0:
        print("It's Saturday")
