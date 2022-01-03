"""
File: proj1.py
Author: Fey Alonge
Date: 10/22/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Baking simulator. Player will buy ingredients to bake various foods. If they don't buy enough ingredients they will lose. They also need to bake the food in a specific order.
 """


STARTING_FUNDS = 80.0
FLOUR_COST = 2.5
EGGS_COST = 1.9
YEAST_COST = 3.25
BUTTER_COST = 1.25
MILK_COST = 2.75
GALLONS_MILK_PER_JUG = 1.0
EGGS_PER_CRATE = 24.0
TBSP_BUTTER_PER_PACK = 64.0
CUPS_FLOUR_PER_BAG = 25.0
CUP_YEAST_PER_BAG = 6.0
FLOUR_REQUIRED = 48.0 + 112.5
EGGS_REQUIRED = 12.0 + 60.0
BUTTER_REQUIRED = 144.0
YEAST_REQUIRED = 39 + 50
MILK_REQUIRED = 18.0
CUPS_IN_GALLON = 16
TSP_IN_CUP = 48
TSP_YEAST_PER_BAG = CUP_YEAST_PER_BAG * TSP_IN_CUP
CUPS_MILK_PER_GALLON = GALLONS_MILK_PER_JUG * CUPS_IN_GALLON

def is_valid_input(index, tasks):
    # checks if the task the user enters is an actual item in their task list
    if index > len(tasks) or index < 0:
        return False
    else:
        return True

def check_items_enough(shopping_cart):
    # This will check if they have enough of each item. Each item will have a certain spot in the "shopping cart" (flour corresponds to 0, eggs to 1, etc.)
    if FLOUR_REQUIRED <= shopping_cart[0] and EGGS_REQUIRED <= shopping_cart[1] and BUTTER_REQUIRED  <= shopping_cart[2] and YEAST_REQUIRED  <= shopping_cart[3] and MILK_REQUIRED <= shopping_cart[4]:
        print("We have everything we need! Ready! Set! Bake!")
        return True
    else:
        if FLOUR_REQUIRED > shopping_cart[0]:
            print("You didn't buy enough flour, we needed", FLOUR_REQUIRED - shopping_cart[0], "more cups.")
        if EGGS_REQUIRED > shopping_cart[1]:
            print("You didn't buy enough eggs, we needed", EGGS_REQUIRED - shopping_cart[1], "more eggs.")
        if BUTTER_REQUIRED > shopping_cart[2]:
            print("You didn't buy enough butter, we needed", BUTTER_REQUIRED - shopping_cart[2], "more tablespoons.")
        if YEAST_REQUIRED > shopping_cart[3]:
            print("You didn't buy enough yeast, we needed", YEAST_REQUIRED - shopping_cart[3], "more cups.")
        if MILK_REQUIRED > shopping_cart[4]:
            print("You didn't buy enough milk, we needed", MILK_REQUIRED - shopping_cart[4], "more cups.")
        print("You did not buy enough ingredients to start baking!")

def go_shopping():
    current_budget = STARTING_FUNDS
    current_flour = 0
    current_eggs = 0
    current_butter = 0
    current_yeast = 0
    current_milk = 0
    shopping_cart = [current_flour, current_eggs, current_butter, current_yeast, current_milk]
    what_to_buy = input("What would you like to purchase? (Enter 'NOTHING' to leave store) ")
    # This will keep asking them for ingredients until they enter NOTHING
    while what_to_buy != "NOTHING":
        if what_to_buy.lower() == "flour":
            how_much = int(input("How many bags of flour would you like? "))
            if how_much < 0:
                print("Please enter a valid number.")
            else:
                # Adding the amount in cups to the shopping cart and subtracting how much they spent from the budget
                shopping_cart[0] += how_much * CUPS_FLOUR_PER_BAG
                current_budget -= FLOUR_COST * how_much
            # If theyre out of money at this point it will check if they have enough stuff with the function
            if current_budget <= 0:
                print("You have run out of money!")
                return check_items_enough(shopping_cart)
            what_to_buy = input("What would you like to purchase? (Enter 'NOTHING' to leave store) ")

        # Repeated the above code for all the ingredients
        if what_to_buy.lower() == "eggs":
            how_much = int(input("How many crates of eggs would you like? "))
            if how_much < 0:
                print("Please enter a valid number.")
            else:
                shopping_cart[1] += how_much * EGGS_PER_CRATE
                current_budget -= EGGS_COST * how_much
            if current_budget <= 0:
                print("You have run out of money!")
                return check_items_enough(shopping_cart)
            what_to_buy = input("What would you like to purchase? (Enter 'NOTHING' to leave store) ")

        if what_to_buy.lower() == "butter":
            how_much = int(input("How many packs of butter would you like? "))
            if how_much < 0:
                print("Please enter a valid number.")
            else:
                shopping_cart[2] += how_much * TBSP_BUTTER_PER_PACK
                current_budget -= BUTTER_COST * how_much
            if current_budget <= 0:
                print("You have run out of money!")
                return check_items_enough(shopping_cart)
            what_to_buy = input("What would you like to purchase? (Enter 'NOTHING' to leave store) ")

        if what_to_buy.lower() == "yeast":
            how_much = int(input("How many bags of yeast would you like? "))
            if how_much < 0:
                print("Please enter a valid number.")
            else:
                shopping_cart[3] += how_much * (TSP_YEAST_PER_BAG)
                current_budget -= YEAST_COST * how_much
            if current_budget <= 0:
                print("You have run out of money!")
                return check_items_enough(shopping_cart)
            what_to_buy = input("What would you like to purchase? (Enter 'NOTHING' to leave store) ")

        if what_to_buy.lower() == "milk":
            how_much = int(input("How many jugs of milk would you like? "))
            if how_much < 0:
                print("Please enter a valid number.")
            else:
                shopping_cart[4] += how_much * CUPS_MILK_PER_GALLON
                current_budget -= MILK_COST * how_much
            if current_budget <= 0:
                print("You have run out of money!")
                return check_items_enough(shopping_cart)
            what_to_buy = input("What would you like to purchase? (Enter 'NOTHING' to leave store) ")

        # Giving an error message if the user gives an invalid response
        if what_to_buy.lower() != "flour" and what_to_buy.lower() != "eggs" and what_to_buy.lower() != "butter" and what_to_buy.lower() != "yeast" and what_to_buy.lower() != "milk" and what_to_buy != "NOTHING":
            print("That is not a valid item.")
            what_to_buy = input("What would you like to purchase? (Enter 'NOTHING' to leave store) ")
    # Checking the user's items if they enter NOTHING
    return check_items_enough(shopping_cart)

def print_task_list(tasks_remaining):
    for i in range(len(tasks_remaining)):
        # For each task left in the list, it will print the corresponding number
        if i == 0:
            print("1 -", end=" ")
            if tasks_remaining[i] == "dough":
                print("Begin the baguette dough")
            elif tasks_remaining[i] == "macrons":
                print("Make the macrons")
            elif tasks_remaining[i] == "croissants":
                print("Make the croissants")
            elif tasks_remaining[i] == "baguettes":
                print("Bake the baguettes")
                        
        elif i == 1:
            print("2 -", end=" ")
            if tasks_remaining[i] == "dough":
                print("Begin the baguette dough")
            elif tasks_remaining[i] == "macrons":
                print("Make the macrons")
            elif tasks_remaining[i] == "croissants":
                print("Make the croissants")
            elif tasks_remaining[i] == "baguettes":
                print("Bake the baguettes")
                        
        elif i == 2:
            print("3 -", end=" ")
            if tasks_remaining[i] == "dough":
                print("Begin the baguette dough")
            elif tasks_remaining[i] == "macrons":
                print("Make the macrons")
            elif tasks_remaining[i] == "croissants":
                print("Make the croissants")
            elif tasks_remaining[i] == "baguettes":
                print("Bake the baguettes")
                        
        elif i == 3:
            print("4 -", end=" ")
            if tasks_remaining[i] == "dough":
                print("Begin the baguette dough")
            elif tasks_remaining[i] == "macrons":
                print("Make the macrons")
            elif tasks_remaining[i] == "croissants":
                print("Make the croissants")
            elif tasks_remaining[i] == "baguettes":
                print("Bake the baguettes")
    what_task = int(input("What task would you like to cross off your list next? "))
    return what_task

def bake():
    tasks = ["dough", "macrons", "croissants", "baguettes"]
    what_task = print_task_list(tasks)
    while len(tasks) > 0:
        if is_valid_input(what_task, tasks):
            if tasks[what_task - 1] == "dough":
                tasks.remove("dough")
                print("Ok, let's knead some baguette dough!")
            elif tasks[what_task - 1] == "macrons":
                if "dough" in tasks:
                    print("We should really start the dough first!")
                else:
                    tasks.remove("macrons")
                    print("Adorable sandwich cookies coming right up!")
            elif tasks[what_task - 1] == "croissants":
                if "dough" in tasks:
                    print("We should really start the dough first!")
                else:
                    tasks.remove("croissants")
                    print("Let's make some flaky crescent goodness!")
            elif tasks[what_task - 1] == "baguettes":
                if len(tasks) != 1:
                    print("Whoa, we should probably do everything else first!")
                else:
                    tasks.remove("baguettes")
                    return "All done!  Let's hope we've PRUEven ourselves worthy"
            what_task = print_task_list(tasks)
        else:
            print("Please enter a valid number.")
            what_task = print_task_list(tasks)

if __name__ == "__main__":
    print("Baker!  You must buy the following with $80:")
    print("For 300 croissants:\n 48 cups of flour\n 12 eggs\n 144 tbsp of butter\n 39 tsp of yeast\n 18 cups of milk")
    print("For 600 macarons:\n 60 eggs")
    print("For 100 baguettes:\n 112.5 cups of flour\n 50 tsp of yeast\n\n")
    print("Welcome to the supermarket!")
    if go_shopping():
        print(bake())
