"""
File: hw5_part1.py
Author: Fey Alonge
Date: 10/8/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Merges two lists of strings together
 """

if __name__ == "__main__":
    # list where the user's words will be stored in
    list_one = []
    # counter to keep track of how many strings the user enters
    num_strings = 0
    word_one = input("Enter words, STOP to stop. ")
    while word_one != "STOP":
        list_one.append(word_one)
        num_strings += 1
        word_one = input("Enter words, STOP to stop. ")

    print("Ok. Now enter", num_strings, "words")
    # counter to keep track of words the user needs to enter
    extra_words = 0
    # another list for the extra words
    list_two = []
    while extra_words < num_strings:
        extra_word_prompt = "Word " + str(extra_words) + ": "
        list_two.append(input(extra_word_prompt))
        extra_words += 1

    print("Now I will magically weave them!")
    for i in range(len(list_one)):
        print(list_one[i])
        print(list_two[i])
