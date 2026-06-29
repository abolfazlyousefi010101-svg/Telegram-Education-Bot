# ----------------------
# board = [1,2,3,4,"X",6,"O",8,9]
# # from termcolor import colored
#
# from terminal_style import *
#
# print(title("=== برنامه من ==="))
# print(success("همه چیز درست است ✅"))
# print(error("خطا رخ داد ❌"))
#
# def print_board():
#     j = 1
#     for i in board:
#         end = " "
#         if j % 3 == 0:
#             end = "\n\n"
#         if i == "X":
#             print(title(f"[{i}]"), end=end)
#         elif i == "O":
#             print(error(f"[{i}]"), end=end)
#         else:
#             print(f"[{i}]", end=end)
#         j += 1
# print_board()
#
#
# # def has_space():
# #     return board.count("X") + board.count("O") != 9
# #
# #
# player , computer = "X" , "O"
# print("player : X\ncomputer : O\n")
#
#-------------------------------------------------------------------------------------------

# import os
# import sys
#
# if sys.platform.startswith("win"):
#     os.system("")
#
# class Style:
#     RESET = "\033[0m"
#     BOLD = "\033[1m"
#     UNDERLINE = "\033[4m"
#
# class Color:
#     RED    = "\033[31m"
#     GREEN  = "\033[32m"
#     YELLOW = "\033[33m"
#     BLUE   = "\033[34m"
#     MAGENTA = "\033[35m"
#     CYAN   = "\033[36m"
#     WHITE  = "\033[37m"
#     BLACK  = "\033[30m"
#
#     BRIGHT_RED    = "\033[91m"
#     BRIGHT_GREEN  = "\033[92m"
#     BRIGHT_YELLOW = "\033[93m"
#     BRIGHT_BLUE   = "\033[94m"
#     BRIGHT_CYAN   = "\033[96m"
#
# class BgColor:
#     RED    = "\033[41m"
#     GREEN  = "\033[42m"
#     YELLOW = "\033[43m"
#     BLUE   = "\033[44m"
#     MAGENTA = "\033[45m"
#     CYAN   = "\033[46m"
#     WHITE  = "\033[47m"
#     BLACK  = "\033[40m"
#
#     BRIGHT_RED   = "\033[101m"
#     BRIGHT_BLUE  = "\033[104m"
#     BRIGHT_GREEN = "\033[102m"
#
# def colored(text, color="", bg="", bold=False, underline=False):
#     style = ""
#     if bold:
#         style += Style.BOLD
#     if underline:
#         style += Style.UNDERLINE
#     style += color + bg
#     return f"{style}{text}{Style.RESET}"
#
# def success(text):
#     return colored(text, Color.GREEN, bold=True)
#
# def error(text):
#     return colored(text, Color.RED, bold=True)
#
# def warning(text):
#     return colored(text, Color.YELLOW, bold=True)
#
# def info(text):
#     return colored(text, Color.BLUE, bold=True)
#
# def title(text):
#     return colored(text, Color.BRIGHT_BLUE, bold=True, underline=True)


#

# ------------------------پزوژه بازی دوز----------------------

# from terminal_style import *
#
#
# board = list(range(1,10))
# winners = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
# moves = ((1,3,7,9), (5,), (2,8,6,4) )


# def print_board():
#     j = 1
#     for i in board:
#         end = " "
#         if j % 3 == 0:
#             end = "\n\n"
#         if i == "X":
#             print(error(f"[{i}]"),end=end)
#         elif i == "O":
#             print(info(f"[{i}]") ,end=end)
#         else:
#             print(f"[{i}]", end=end)
#         j += 1
#
#
# def make_move(brd, plyr, mve, undo=False):
#     if can_move(brd,mve):
#         brd[mve-1] = plyr
#         win = is_winner(brd, plyr)
#         if undo:
#             brd[mve-1] = mve
#         return True, win
#     return False, False
#
#
# def can_move(brd,mve):
#     if mve in range(1,10) and isinstance(brd[mve-1], int):
#         return True
#     return False
#
#
# def is_winner(brd, plyr):
#     win = True
#     for tup in winners:
#         win = True
#         for j in tup:
#             if brd[j] != plyr:
#                 win = False
#                 break
#         if win:
#             break
#     return win
#
#
# def has_empty_space():
#     return board.count("X") + board.count("O") != 9
#
#
# def computer_move():
#     mv = -1
#     # آیا خود کامپیوتر میتواند برنده شود یا نه؟
#     for i in range(1, 10):
#         if make_move(board, computer, i , True)[1]:
#             mv = i
#             break
#     #اگر کاربر بتواند برنده شود جلوی او را بگیر
#     if mv == -1:
#         for j in range(1, 10):
#             if make_move(board, player, j, True)[1]:
#                 mv = j
#                 break
#     #حرکت کن
#     if mv == -1:
#         for tup in moves:
#             for number in tup:
#                 if mv == -1 and can_move(board, number):
#                     mv = number
#                     break
#     return make_move(board, computer, mv)
#
#
# player, computer = "X" , "O"
# print("player: X\ncomputer: O\n")
# while has_empty_space():
#     print_board()
#     move = int(input("choose your move(1-9): "))
#     moved, won = make_move(board, player, move)
#     if not moved:
#         print("wrong number! Try again!")
#         continue
#     if won:
#         print(success("you win!"),"\n")
#         break
#     elif computer_move()[1]:
#         print(warning("you lose!"),"\n")
#         break
#
# print_board()
#











































