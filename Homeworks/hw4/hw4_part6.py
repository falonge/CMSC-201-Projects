"""
File: hw4_part6.py
Author: Fey Alonge
Date: 10/1/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Creates a box by counting up from 0
 """

if __name__ == "__main__":
    WIDTH = int(input("Enter a width: "))
    HEIGHT = int(input("Enter a height: "))
    box = list(range(WIDTH * HEIGHT)) # creates a list counting from 0 to the area of the box

    for i in range(len(box)):
        # makes a new line if the number goes over the edge of the "box"
        if box[i] % WIDTH == 0:
            print()
            print(box[i], end=" ")
        else:
            print(box[i], end=" ")
