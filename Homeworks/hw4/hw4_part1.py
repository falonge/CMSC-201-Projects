"""
File: hw4_part1.py
Author: Fey Alonge
Date: 10/1/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Hailstone movement simulation
 """

if __name__ == "__main__":
    height = int(input("Please enter the starting height of the hailstone: "))
    while height != 0 and height != 1:
        print("Hailstone is currently at height", int(height))
        if height % 2 == 0:
            height /= 2
        elif height % 2 != 0:
            height *= 3
            height += 1

    if height == 0 or height == 1:
        print("Hailstone stopped at height", int(height))
