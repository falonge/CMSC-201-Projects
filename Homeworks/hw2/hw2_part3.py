"""
File: hw2_part3.py
Author: Fey Alonge
Date: 9/18/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: "Pocket Monster Battles" game.
 """

monster_one = input("What is the name of the first monster? ")
power_level_one = int(input("What is the power level of the first monster? "))
monster_two = input("What is the name of the second monster? ")
power_level_two = int(input("What is the power level of the second monster? "))
if power_level_one > power_level_two:
        if (power_level_two*2) <= power_level_one:
                    print(monster_one, "wins!")
                    print(monster_one, "was super efficacious!")
        else:
                    print(monster_one, "wins!")
elif power_level_two > power_level_one:
        if (power_level_one*2) <= power_level_two:
                    print(monster_two, "wins!")
                    print(monster_two, "was super efficacious!")
        else:
                    print(monster_two, "wins!")
elif power_level_one == power_level_two:
        print("It's a draw!")
