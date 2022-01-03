"""
File: hw6_part2.py
Author: Fey Alonge
Date: 11/11/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Zips two lists together using recursion 
 """
def zip_lists(list_one, list_two, current_list, index):
    current_list.append(list_one[index])
    current_list.append(list_two[index])
    index += 1
    if index == len(list_one) - 1:
        return current_list
    else:
        return zip_lists(list_one, list_two, current_list, index)

if __name__ == "__main__":
    word_list_one = []
    words_entered = 0
    user_input = ""
    while user_input != "STOP":
        user_input = input("Enter words, STOP to stop. ")
        word_list_one.append(user_input)
        if user_input != "STOP":
            words_entered += 1
    print("Ok. Now enter", words_entered, "more words.")

    word_list_two = []
    words_left = 1
    while words_left <= words_entered:
        input_message = "Word " + str(words_left) + ": "
        user_input = input(input_message)
        word_list_two.append(user_input)
        words_left += 1

    if words_entered  == 0:
        print("[]")
    else:
        print(zip_lists(word_list_one, word_list_two, [], 0))
