"""
File: hw2_part5.py
Author: Fey Alonge
Date: 9/18/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Botanical classification system 
 """

bugs = input("Does the plant eat bugs? ")
if bugs == "yes":
        trap = input("Does the plant use a pitfall trap or snap jaws? ")
        if trap == "pitfall trap":
            print("Oh, interesting. That is a Nepenthes. Don't drink from a pitcher plant.")
        elif trap == "snap jaws":
            print("Watch those fingers! You got a Dionaea muscipula: the venus fly trap!")
elif bugs == "no":
    petals = int(input("How many petals does it have? "))
    if petals > 7:
        height = int(input("How many cm tall is it? "))
        if height <= 300:
            print("Hmm, that is some kind of Asteracea. Premium specimen of photosynthetic evolution!")
        else:
            print("Oh, that is a Helianthus annuus, or sunflower for the uninitiated.")
    elif petals == 5:
        print("Oh, you have an Orchidaceae, known by its friends as an Orchid.")
    elif petals == 3:
        print("Irises are nice, and that's what you have.")
    else:
        print("I don't know what that is...")
