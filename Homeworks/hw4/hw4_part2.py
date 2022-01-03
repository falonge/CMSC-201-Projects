"""
File: hw4_part2.py
Author: Fey Alonge
Date: 10/1/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Integer division calculator
 """

if __name__ == "__main__":
    num_one = int(input("Please enter the first number: "))
    num_one_copy = num_one # makes a copy of num_one so we can print it at the end
    num_two = int(input("Please enter the second number: "))
    counter = 0 # This will keep count of how many times we subtract

    while num_one >= num_two:
            num_one -= num_two
            counter +=1
    print(num_one_copy, "//", num_two, "=", counter)
