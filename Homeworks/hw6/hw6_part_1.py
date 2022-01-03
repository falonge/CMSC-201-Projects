"""
File: hw6_part1.py
Author: Fey Alonge
Date: 11/11/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Integer divides two numbers using recursion.
 """


def integer_divide(num_one, num_two, index):
    if num_one - num_two < 0:
        return index
    else:
        num_one -= num_two
        index += 1
        return integer_divide(num_one, num_two, index)

    
if __name__ == "__main__":
    num_one = int(input("Enter a number: "))
    num_two = int(input("Enter another number: "))
    print(integer_divide(num_one, num_two, 0))
