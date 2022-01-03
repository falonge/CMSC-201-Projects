"""
File: hw5_part3.py
Author: Fey Alonge
Date: 10/8/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Draws a right triangle
 """

if __name__ == "__main__":
    height = int(input("What is the height of the triangle? "))
    symbol = input("What is the symbol for the triangle? ")
    # will keep track of how many lines have been completed and how many symbols have been completed for each line respectively
    current_line = 1
    current_symbol = 1

    while current_line <= height:
            while current_symbol <= current_line:
                print(symbol, end="")
                current_symbol += 1
            current_line += 1
            current_symbol = 1
            print("\n", end="")
