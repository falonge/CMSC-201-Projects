"""
File: hw4_part5.py
Author: Fey Alonge
Date: 10/1/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Prints numbers counting up to a limit, with special messages at certain numbers.
 """

if __name__ == "__main__":
    UPPER_LIMIT = int(input("What is the upper limit? "))
    current_value = UPPER_LIMIT-(UPPER_LIMIT-1) # the program will print the numbers by subtracting this variable, which wil change using a while loop.
    while current_value <= UPPER_LIMIT:
            if current_value % 3 == 0 and current_value % 4 == 0:
                print("This is a very special time, savor it.")
            elif current_value % 3 == 0:
                print("One time I saw three hawks piled on a cactus.")
            elif current_value % 4 == 0:
                print("Four? What is it good for? Absolutely nothing!")
            else:
                print(current_value)
            current_value += 1
