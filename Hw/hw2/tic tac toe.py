import os
import random
class Board:
    def __init__(self):
        self.board = ["-", "-", "-",
                      "-", "-", "-",
                      "-", "-", "-"]
    def disply(self):
        print("\n")
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2] + "     1 | 2 | 3")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5] + "     4 | 5 | 6")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8] + "     7 | 8 | 9")
        print("\n")
    def update_cell(self, cell_nu, player):
        if self.board[cell_nu] == "-":
            self.board[cell_nu] = player
    def winner_check(self, player):
        for list in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [2,4,6], [0,4,8]]:
            result = True
            for cell_nu in list:
                if self.board[cell_nu] != player:
                    result = False
            if result == True:
                return True
        return False
    def check_for_tie(self):
        board_full = 0
        for cell in self.board:
            if cell != "-":
                board_full += 1
        if board_full == 9:
            return True
        else:
            return False
    def reset(self):
        self.board = ["-", "-", "-",
                      "-", "-", "-",
                      "-", "-", "-"]
    def comp_move_lvl1(self, player):
        i = random.randint(0, 9)
        if self.board[i] == "-":
            self.update_cell(i, player)
        else:
            i = random.randint(0, 8)
    def comp_move_lvl2(self, player):
        if self.board[4] == "-":
            self.update_cell(4, player)
        elif self.board[0] == "-":
            self.update_cell(0, player)
        elif self.board[1] == "-":
            self.update_cell(1, player)
        elif self.board[2] == "-":
            self.update_cell(2, player)
        elif self.board[5] == "-":
            self.update_cell(5, player)
        elif self.board[8] == "-":
            self.update_cell(8, player)
        elif self.board[4] == "-":
            self.update_cell(4, player)
        elif self.board[6] == "-":
            self.update_cell(6, player)
        elif self.board[3] == "-":
            self.update_cell(3, player)
        elif self.board[7] == "-":
            self.update_cell(7, player)

board = Board()

level = input('choose yr difficulty: (easy/hard) > ')


def refresh_screen():
    os.system('cls')
    board.disply()

while True:
    refresh_screen()

    x_choice = int(input('\nX ; plz choose 1 - 9 :'))-1

    board.update_cell(x_choice, "X")

    refresh_screen()

    if board.winner_check("X"):
        print('\nX is winner\n')
        play_again = input('do you wanna to play again? (Y/N) ').upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    if board.check_for_tie():
        print('\nTie game\n')
        play_again = input('do you wanna to play again? (Y/N) ').upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    if level == "easy":
        board.comp_move_lvl1("O")
    else:
        board.comp_move_lvl2("O")
    refresh_screen()

    if board.winner_check("O"):
        print('\nO is winner\n')
        play_again = input('do you wanna to play again? (Y/N) ').upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    if board.check_for_tie():
        print('\nTie game\n')
        play_again = input('do you wanna to play again? (Y/N) ').upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break