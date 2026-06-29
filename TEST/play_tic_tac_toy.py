# ------------------------پزوژه بازی دوز----------------------
board = list(range(1,10))

def print_board():
    j = 1
    for i in board:
        end = " "
        if j % 3 == 0:
            end = "\n\n"
        print(f"[{i}]", end=end)
        j += 1
print_board()

def has_empty_space():
    return board.count("X") + board.count("O") != 9


player, computer = "X" , "O"
print("player: X\ncomputer: O\n")

# while has_empty_space():
#     print_board()































































































































