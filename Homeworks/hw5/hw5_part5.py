"""
File: hw5_part5.py
Author: Fey Alonge
Date: 10/8/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Prints words backwards that the user inputs
 """

if __name__ == "__main__":
    word_list = []
    num_words = int(input("How many words would you like to turn backwards: "))
    words_entered = 1
    while words_entered <= num_words:
        new_word_prompt = "Please enter current_string #" + str(words_entered) +" : "
        word_list.append(input(new_word_prompt))
        words_entered += 1

    # creates a new word list in reverse order of the one given by the user
    new_word_list = []
    for i in range(len(word_list)):
        reversed_word = []
        current_string = word_list[i]
        index = len(current_string)
        while index > 0:
            reversed_word.append(current_string[index-1])
            index -= 1
        new_word_list.append("".join(reversed_word))

    for i in range(len(new_word_list)):
        # list so the program can compare the size to the current word and print a new line when the word is complete
        new_line = []
        # will keep track of the words in reverse order
        word_reverse_order = len(new_word_list)-(1+i)
        for j in new_word_list[word_reverse_order]:
            new_line.append(j)
            if len(new_line) == len(new_word_list[word_reverse_order]):
                new_line = "".join(new_line)
                reversed_sentence = "The string '" + str(word_list[len(word_list) - (1 + i)]) + "' reversed is '" + new_line + "'."
                print(reversed_sentence)
