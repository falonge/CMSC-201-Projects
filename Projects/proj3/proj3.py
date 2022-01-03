"""
File: proj3.py
Author: Fey Alonge
Date: 12/4/2019
Section: 33
E-mail: falonge1@umbc.edu
Description: Score keeper for Go board game
 """

def make_board(board_file):
    board_list = []
    for line in board_file:
        new_line = []
        for character in line:
            new_line.append(character)
        board_list.append(new_line)
    return board_list


def fill_board(board_list):
    for i in range(len(board_list)):
        for j in range(len(board_list[i])):
            if j != 0:
                if board_list[i][j] == "+" and board_list[i][j-1] == "O":
                    board_list[i][j] = "O"
                elif board_list[i][j] == "+" and board_list[i][j-1] == "X":
                    board_list[i][j] = "X"
    for i in range(len(board_list)):
        for j in range(len(board_list[i])):
            if j != len(board_list[i])-1:
                if board_list[i][j] == "+" and board_list[i][j+1] == "O":
                    board_list[i][j] = "O"
                    board_list = fill_board(board_list)
                elif board_list[i][j] == "+" and board_list[i][j+1] == "X":
                    board_list[i][j] = "X"
                    board_list = fill_board(board_list)
    return board_list


def print_board(board_list):
    for i in range(len(board_list)):
        for j in range(len(board_list[i])):
            print(board_list[i][j], end="")


def get_scores(board_list):
    x_count = 0
    o_count = 0
    for i in range(len(board_list)):
        for j in range(len(board_list[i])):
            if board_list[i][j] == "X":
                x_count += 1
            if board_list[i][j] == "O":
                o_count += 1
    return [x_count, o_count]


if __name__ == "__main__":
    board = open(input("What is the file name? "))
    print("We are scoring this board:")
    board = (make_board(board))
    print_board(board)
    print("\nThis is the colored board:")
    board = fill_board(board)
    print_board(board)
    scores = get_scores(board)
    print("\nBlack scored:", scores[0])
    print("White scored:", scores[1])
