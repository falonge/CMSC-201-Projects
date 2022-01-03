"""
File: hw3_part3.py
Author: Fey Alonge
Date: 9/24/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Children's name game
 """

if __name__=='__main__':
    
    person_one = input("Who is the first person? ")
    person_two = input("Who is the second person? ")
    person_three = input("Who is the third person? ")
    person_four = input("Who is the fourth person? ")
    person_five = input("Who is the fifth person? ")
    people = [person_one, person_two, person_three, person_four, person_five]
    # making a seperate list to keep track of people who the user mentioned in the follow up questions
    people_included = []
    # making two conditions: exists checks to see if the person exists in the list and all_questions checks to see if all the questions have been answered.
    exists = True
    all_questions = False
    candy = input("Which of these people would you give your last piece of candy? ")
    for person in people:
        if candy == person:
            people_included.append(person)
            trip = input("With which of these people would you go on a 12 hour road trip? ")
            for person in people:
                if trip == person:
                    people_included.append(person)
                    tennis = input("With which of these people would you play tennis on a yacht? ")
                    for person in people:
                        if tennis == person:
                            people_included.append(person)
                            print("I feel bad for these people:")
                            for person in people:
                                if person not in people_included:
                                    print(person)
                                    # all_questions is set to True when all the questions have been answered and there were no false names.
                                    all_questions = True
                                    
    # if a fake name is entered or all the questions have been answered, then the loop will exit to here. The code then checks to see if whether a fake name has been entered or if the questions have been answered.
    for person in people:
        if candy != person or trip != person or tennis != person:
            exists = False
    if all_questions == True:
        exists = True
                                                
    if exists == False:
        print("Hey, I don't know who that is! That's cheating!")
                                                                                                                                                                                                                                                                                                                                                                                        
