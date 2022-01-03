"""
File: hw5_part4.py
Author: Fey Alonge
Date: 10/8/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: "Enlolinator". Puts "ol" after every consonant not followed by a vowel
 """

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    for i in range(len(sentence)):
        if i == len(sentence) - 1 and sentence[i] in consonants:
            print(sentence[i], end="ol")
        elif sentence[i].lower() in consonants and sentence[i+1].lower() not in consonants:
            print(sentence[i], end="ol")
        else:
            print(sentence[i], end="")
