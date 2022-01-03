"""
File: icecream.py
Author: Fey Alonge
Date: 9/24/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Uses loops to print out ice cream flavors and toppings
 """

ice_cream_flavors = ["vanilla", "strawberry", "chocolate"]
toppings = ["caramel", "marshmallow", "gummi bears"]

for flavor in ice_cream_flavors:
        if flavor != "strawberry":
            print(flavor, "is tasty with caramel")
            print(flavor, "is tasty with marshmallow")
            print(flavor, "is tasty with gummi bears")
        else:
            print("strawberry is fine on its own!")
