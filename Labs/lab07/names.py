"""
File:         names.py
Author:       Fey Alonge
Date:         10/22/2019
Section:      33
E-mail:       falonge1@umbc.edu
Description:  Gets list of names from user and states how many total leters are in the list.
"""

def sum_list(numbers):
    num_total = 0
    for number in numbers:
        num_total += number
    return num_total


def get_string_lengths(strings):
    list_string_lengths = []
    for string in strings:
        list_string_lengths.append(len(string))
    return list_string_lengths


def get_names():
    list_names = []
    ask_new_name = input("Enter a name, STOP to stop: ")
    while ask_new_name != "STOP":
        list_names.append(ask_new_name)
        ask_new_name = input("Enter a name, STOP to stop: ")
    return list_names


if __name__ == '__main__':
    kitties = [
        "Jules",
        "Stubby",
        "Tybalt",
        "Scooter",
        "KC",
        "Garfield",
        "Bucky"
    ]

print("There are", sum_list(get_string_lengths(kitties)), "letters in kittens.")


puppers = [
        "Charlie",
        "Chuck",
        "Chuckadero",
        "Char",
        "Charmander",
        "Charles, Lord of Hearts, King of Snuggles"
    ]
print("There are", sum_list(get_string_lengths(puppers)), "letters in puppers." )

user_names = get_names()
print("There are", sum_list(get_string_lengths(user_names)), "letters in the names you entered")

