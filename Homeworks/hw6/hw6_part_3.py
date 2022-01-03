"""
File: hw6_part3.py
Author: Fey Alonge
Date: 11/12/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Takes a hidden message inside an encrypted message and replaces it with a new hidden message
 """

def replace_hidden_message(encrypted_message, hidden_message, new_hidden_message):
    """
    Checks to see if the first letters of the encrypted message and hidden message are the same, and then replaces the letter with the new letter from the new hidden message. After that it cuts off the first letter of all three messages. (This is how I iterate through the message)
    """
    if len(hidden_message) > 0 and encrypted_message[0] == hidden_message[0]:
        encrypted_message = new_hidden_message[0] + encrypted_message[1: len(encrypted_message)]
        hidden_message = hidden_message[1: len(hidden_message)]
        new_hidden_message = new_hidden_message[1: len(new_hidden_message)]
    new_encrypted_message = encrypted_message[1: len(encrypted_message)]
    # Prevents the program from crashing when it hits the end
    if len(new_encrypted_message) == 0:
        return encrypted_message
    # Calls the function again and adds on the bit of the encrypted message that was changed
    return encrypted_message[0: (len(encrypted_message) - len(new_encrypted_message))] + replace_hidden_message(new_encrypted_message, hidden_message, new_hidden_message)


if __name__ == "__main__":
    encrypted_message = input("Give me a string with a hidden message in it: ")
    hidden_message = input("Give me the hidden message: ")
    new_hidden_message = input("What do you want the new hidden message to be? ")
    
    if len(hidden_message) != len(new_hidden_message):
            print("The new message must be the same length. Good day.")
    else:
            print(replace_hidden_message(encrypted_message, hidden_message, new_hidden_message))
