"""
File: proj2.py
Author: Fey Alonge
Date: 11/5/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Sim game
 """

from proj2_ui import print_board

# This will put the points that the user inputs  in order of lowest to highest to make them easier to work with
def arrange_line(point_1, point_2):
    if point_1 < point_2:
        return [point_1, point_2]
    else:
        return [point_2, point_1]

# This will check if the line the buser entered has already been made, either in their list or the other player's
def line_is_copy(line, line_list):
    if line in line_list:
        return True
    else:
        return False

# This will check if they made a triangle by running through a list of all possible triangle combinations
def made_a_triangle(line_list):
        triangle_combinations = [[[1, 2], [2, 3], [1, 3]], [[2, 3], [3, 4], [2, 4]], [[3, 4], [4, 5], [3, 5]],
                                 [[4, 5], [5, 6], [4, 6]], [[5, 6], [1, 6], [1, 5]], [[2, 6], [1, 2], [1, 6]],
                                 [[1, 2], [2, 4], [1, 4]], [[2, 3], [3, 6], [2, 6]], [[3, 4], [1, 4], [1, 3]],
                                 [[4, 5], [1, 5], [1, 4]], [[5, 6], [2, 6], [2, 5]], [[1, 6], [1, 3], [3, 6]],
                                 [[1, 3], [3, 5], [1, 5]], [[2, 4], [4, 6], [6, 2]], [[1, 2], [2, 5], [1, 5]],
                                 [[2, 3], [3, 5], [2, 5]], [[3, 4], [4, 6], [3, 6]], [[4, 5], [2, 5], [2, 4]],
                                 [[5, 6], [3, 6], [3, 5]], [[1, 6], [4, 6], [1, 4]]]
        for i in range(len(triangle_combinations)):
            counter = 0
            for j in range(len(triangle_combinations[i])):
                if triangle_combinations[i][j] in line_list:
                    counter += 1
                if counter == 3:
                    return True
        return False

# This will make player 2 pick a different character from player 1
def check_same_character(character_1, character_2):
        while character_1 == character_2:
            print("You can't use the same character as player 1.")
            character_2 = input("Hello, what character would player 2 like to use? ")

# This will test if the user gave some bad input, whether they don't type with the right format, they pick a number that's not between 1 and 6, or they draw a line to itself. It will also test if they're drawing a line over their own or the other player's lines.
def check_input(line, turn, p1_lines, p2_lines):
    # A list of the only points they're allowed to go to
    valid_lines = [1, 2, 3, 4, 5, 6]
    if len(line) != 3 or line[1] != " ":
        print("Invalid format. To make a line, type two numbers with a space between")
        return False
    elif int(line[0]) not in valid_lines or int(line[2]) not in valid_lines:
        print("You can only pick numbers between 1 and 6.")
        return False
    elif line[0] == line[2]:
        print("You can't draw a line to itself.")
        return False
    else:
        if turn == 1:
        # After confirming the points are valid, it will test to see if the line is okay
            test_line = arrange_line(int(line[0]), int(line[2]))
            if line_is_copy(test_line, p1_lines):
                print("You can't make a line over one you already made.")
                return False
            elif line_is_copy(test_line, p2_lines):
                print("You can't make a line over one of player 2's lines")
                return False
            else:
                return True
        elif turn == 2:
            test_line = arrange_line(int(line[0]), int(line[2]))
            if line_is_copy(test_line, p2_lines):
                print("You can't make a line over one you already made.")
                return False
            elif line_is_copy(test_line, p1_lines):
                print("You can't make a line over one of player 1's lines")
                return False
            else:
                return True

# The main part of the program. This will start the game, print the board after every turn, and check if either of the players lost after they make their move.
def play_sim():
    p1_character = input("Hello, what character would player 1 like to use? ")
    p2_character = input("Hello, what character would player 2 like to use? ")
    p1_lines = []
    p2_lines = []
    check_same_character(p1_character, p2_character)
    game_over = False
    player_turn = 1
    while not game_over:
        if player_turn == 1:
            correct_input = False
            # Keeps asking for a new line until the player enters a valid one
            while not correct_input:
                new_line = input("Enter a line for player 1. ")
                correct_input = check_input(new_line, player_turn, p1_lines, p2_lines)
            p1_lines.append(arrange_line(int(new_line[0]), int(new_line[2])))
            print_board(p1_lines, p1_character, p2_lines, p2_character)
            if made_a_triangle(p1_lines):
                game_over = True
            player_turn = 2
        elif player_turn == 2:
            correct_input = False
            while not correct_input:
                new_line = input("Enter a line for player 2. ")
                correct_input = check_input(new_line, player_turn, p1_lines, p2_lines)
            p2_lines.append(arrange_line(int(new_line[0]), int(new_line[2])))
            print_board(p1_lines, p1_character, p2_lines, p2_character)
            if made_a_triangle(p2_lines):
                game_over = True
            player_turn = 1
    if player_turn == 2:
        print("Game over. Player 1 loses.")
    elif player_turn == 1:
        print("Game over. Player 2 loses.")



if __name__ == "__main__":
    play_sim()
