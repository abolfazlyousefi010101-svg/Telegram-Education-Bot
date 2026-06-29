#
# ------------------------پزوژه بازی دوز----------------------
from terminal_style import *


# board = list(range(1,10))
# winners = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
# moves = ((1,3,7,9),(5,), (2,8,6,4) )
#
#
#
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


# --------------------------------مرور-----------------------------

# (7)
# from terminal_style import *
#(5)
# board = list(range(1,10))
# حالت هایی که کاربر انسان میتواند برنده باشد
# (16)
# winners = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))


# تابعی مینویسیم که هرگاه دلمان خواست بتوانیم تخته دوز را چاپ کنیم با رنگ های مختلف
# (6)
# def print_board():
#     j = 1
#     for i in board:
#         end = " "
#         if j % 3 == 0:
#             end = "\n\n"
#         if i == "X":
#             print(colored(f"[{i}]", "red"), end=end)
#         elif i == "O":
#             print(colored(f"[{i}", "blue"), end=end)
#         else:
#             print(f"[{i}]", end=end)
#         j += 1

#یک تابع مینویسیم که دو متغیر را پوشش میدهد و آن ها را برمیگرداند یکی move به معنای حرکت کردن یا نکردن است و دیگری win به معنای برنده شدن یا نشدن است که هر دو این ها که هرکدام دو حالت دارند با True و False مشخص میشود
# کار undo این است که یک حر کت تستی را انجام دهد بجای کار بر و ببیند ایا کاربر برنده میشود یا نه مثلا اگر برنده میشود جلویش را بگیرد
#(10)

# def make_move(brd, plyr, mve, undo=False):
    # حالا اگر بتواند حر کت کند یک ماجرا است و اگر نتواند یک ماجرا دیگر
    # (11)
    # if can_move(brd, mve):
    #     brd[mve-1] = plyr
        # متغیر برای برنده بودن یا نبودن کاربر
        # (14)
        # win = is_winner
        # برای undo است کهبه صورت دیفالت فالس است و ما آن را ترو در نظر میگیریم تا به عنوان تست هرچه که برداشت بزاره سرجاش
        #(18)
        # if True:
        #     brd[mve-1] = mve
        # return True, win
    # return False, False


# تابعی که بررسی میکند آیا کاربر میتواند حرکتی انجام دهد یا نه چون مثلا اگر کابر اشتباهی عدد 100 را بزند ما که عدد 100 نداریم پس مسلما نباید حرکتی انجام شود
# (12)
# def can_move(brd,mve):
    # کاربرد isinstance: خانه ای که کاربر قراره حرکت کند را بررسی میکند که ایا اینتیجر یا همان عدد هست یا نه اگر عدد نباشد یعنی اون خونه هرکت انجام شده از قبل و ما حرکت جدید را در خانه دیگر انجام میدهیم(بجای عدد x یا o ایجاد میشود
    # (13)
    # if mve in range(1,10) and isinstance(brd[mve-1], int):
    #     return True
    # return False

# تابعی برای فرض به برنده بودن کاربر انسان
# (15)
# def is_winner(brd, plyr):
#     win = True
    # حلقه ای برای مشخص کردن برنده ها  بازنده ها
    # (17)
    # این خلقه مشخص میکند که اگر کاربر انسان اون تاپل هایی که درون متغیر بودند را که جزو برنده ها بود انتخاب نکرده باشد برنامه کاربر را بازنده اعلام کرده و از بازی خارج میکند
    # for tup in winners:
    #     win = True
    #     for j in tup:
    #         if brd[j] != plyr:
    #             win = False
    #             break
        # اگر هم که کاربر انسان براساس تاپل های مشخص شده برنده شده باشد باز هم بریکمیدهد و از بازی خارج میشود
        # if win:
        #     break
    # return True

# تابغی که چک میکند آیا هر بار خانه خالی داریم یانه اگر حلقه تشخیص دهد که بازی ادامه دارد بازی کن و کامپیوتر میتوانند بازی را ادامه دهند
# (1)

# def has_empty_spase():
#     return board.count("X") + board.count("O") != 9

# حالا تابع را میدهیم به حلقه تکرار شونده while و اگر Ture داد یعنی بازی ادامه دارد و جای خالی و جود دارد و اگر False بود که برعکس
# (2)

# player, computer = "X", "O"
# print("Player: X\nComputer: O\n ")

# صدا زدن تابع در حلقه تکراری
# (3)

# while has_empty_spase():

    #صدازدن تخته دوز
    # (4)

    # print_board()

    #وارد کردن یک عدد برای صفخه ذوز توسظ کاربر انسان
    # (8)

    # move = int(input("choose your move(1-9): "))
    #دو متغیر یکی برای حرکت کردن یا نکردن و دیگری برای برنده شدن یا نشدن که هر دو براساس True و False کار میکنند
    # (9)

    # moved , win = make_move(board, player, move)



# --------------------پایان--------------------------









































































































