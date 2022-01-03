"""
File: hw3_part4.py
Author: Fey Alonge
Date: 9/24/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Silly statement generator 
 """

if __name__=="__main__":
    animal_one = input("What is the first animal? ")
    animal_two = input("What is the second animal? ")
    animal_three = input("What is the third animal? ")
    clothing_one = input("What is the first piece of clothing? ")
    clothing_two = input("What is the first piece of clothing? ")
    clothing_three = input("What is the first piece of clothing? ")

    animals = [animal_one, animal_two, animal_three]
    clothes = [clothing_one, clothing_two, clothing_three]

    for animal in animals:
            for item in clothes:
                        print(animal, "is wearing a", item, "-- crazy!")
