import random
mines = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
]
board = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
]
board_view = [
    "_", "_", "_", "_", "_", "_", "_", "_",
    "_", "_", "_", "_", "_", "_", "_", "_",
    "_", "_", "_", "_", "_", "_", "_", "_",
    "_", "_", "_", "_", "_", "_", "_", "_",
    "_", "_", "_", "_", "_", "_", "_", "_",
    "_", "_", "_", "_", "_", "_", "_", "_",
    "_", "_", "_", "_", "_", "_", "_", "_",
    "_", "_", "_", "_", "_", "_", "_", "_"
]
move = ""
for i in range(0, 10):
    while True:
        a = random.randint(0, 63)
        if mines[a] == 0:
            mines[a] = 1
            break
        else:
            continue
for i in range(0, 64):
    if i == 0:
        if mines[0] == 0:
            board[0] = mines[1] + mines[8] + mines[9]
        else:
            board[0] = 9
    elif i > 0 and i < 7:
        if mines[i] == 0:
            board[i] = mines[i - 1] + mines[i + 1] + mines[i + 7] + mines[i + 8] + mines[i + 9]
        else:
            board[i] = 9
    elif i == 7:
        if mines[7] == 0:
            board[7] = mines[6] + mines[14] + mines[15]
        else:
            board[7] = 9
    elif i == 8 or i == 16 or i == 24 or i == 32 or i == 40 or i == 48:
        if mines[i] == 0:
            board[i] = mines[i - 8] + mines[i - 7] + mines[i + 1] + mines[i + 8] + mines[i + 9]
        else:
            board[i] = 9
    elif (i > 8 and i < 15) or (i > 16 and i < 23) or (i > 24 and i < 31) or (i > 32 and i < 39) or (i > 40 and i < 47) or (i > 48 and i < 55):
        if mines[i] == 0:
            board[i] = mines[i - 9] + mines[i - 8] + mines[i - 7] + mines[i - 1] + mines[i + 1] + mines[i + 7] + mines[i + 8] + mines[i + 9]
        else:
            board[i] = 9
    elif i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55:
        if mines[i] == 0:
            board[i] = mines[i - 9] + mines[i - 8] + mines[i - 1] + mines[i + 7] + mines[i + 8]
        else:
            board[i] = 9
    elif i == 56:
        if mines[56] == 0:
            board[56] = mines[48] + mines[49] + mines[57]
        else:
            board[56] = 9
    elif i > 56 and i < 63:
        if mines[i] == 0:
            board[i] = mines[i - 9] + mines[i - 8] + mines[i - 7] + mines[i - 1] + mines[i + 1]
        else:
            board[i] = 9
    elif i == 63:
        if mines[63] == 0:
            board[63] = mines[54] + mines[55] + mines[62]
        else:
            board[63] = 9
def print_board():
    print(" _a_b_c_d_e_f_g_h_")
    print(f"1|{board_view[0]}|{board_view[1]}|{board_view[2]}|{board_view[3]}|{board_view[4]}|{board_view[5]}|{board_view[6]}|{board_view[7]}|")
    print(f"2|{board_view[8]}|{board_view[9]}|{board_view[10]}|{board_view[11]}|{board_view[12]}|{board_view[13]}|{board_view[14]}|{board_view[15]}|")
    print(f"3|{board_view[16]}|{board_view[17]}|{board_view[18]}|{board_view[19]}|{board_view[20]}|{board_view[21]}|{board_view[22]}|{board_view[23]}|")
    print(f"4|{board_view[24]}|{board_view[25]}|{board_view[26]}|{board_view[27]}|{board_view[28]}|{board_view[29]}|{board_view[30]}|{board_view[31]}|")
    print(f"5|{board_view[32]}|{board_view[33]}|{board_view[34]}|{board_view[35]}|{board_view[36]}|{board_view[37]}|{board_view[38]}|{board_view[39]}|")
    print(f"6|{board_view[40]}|{board_view[41]}|{board_view[42]}|{board_view[43]}|{board_view[44]}|{board_view[45]}|{board_view[46]}|{board_view[47]}|")
    print(f"7|{board_view[48]}|{board_view[49]}|{board_view[50]}|{board_view[51]}|{board_view[52]}|{board_view[53]}|{board_view[54]}|{board_view[55]}|")
    print(f"8|{board_view[56]}|{board_view[57]}|{board_view[58]}|{board_view[59]}|{board_view[60]}|{board_view[61]}|{board_view[62]}|{board_view[63]}|")
def print_board_n(): #debug
    print(" _a_b_c_d_e_f_g_h_")
    print(f"1|{board[0]}|{board[1]}|{board[2]}|{board[3]}|{board[4]}|{board[5]}|{board[6]}|{board[7]}|")
    print(f"2|{board[8]}|{board[9]}|{board[10]}|{board[11]}|{board[12]}|{board[13]}|{board[14]}|{board[15]}|")
    print(f"3|{board[16]}|{board[17]}|{board[18]}|{board[19]}|{board[20]}|{board[21]}|{board[22]}|{board[23]}|")
    print(f"4|{board[24]}|{board[25]}|{board[26]}|{board[27]}|{board[28]}|{board[29]}|{board[30]}|{board[31]}|")
    print(f"5|{board[32]}|{board[33]}|{board[34]}|{board[35]}|{board[36]}|{board[37]}|{board[38]}|{board[39]}|")
    print(f"6|{board[40]}|{board[41]}|{board[42]}|{board[43]}|{board[44]}|{board[45]}|{board[46]}|{board[47]}|")
    print(f"7|{board[48]}|{board[49]}|{board[50]}|{board[51]}|{board[52]}|{board[53]}|{board[54]}|{board[55]}|")
    print(f"8|{board[56]}|{board[57]}|{board[58]}|{board[59]}|{board[60]}|{board[61]}|{board[62]}|{board[63]}|")
def print_mines(): #debug
    print(" _a_b_c_d_e_f_g_h_")
    print(f"1|{mines[0]}|{mines[1]}|{mines[2]}|{mines[3]}|{mines[4]}|{mines[5]}|{mines[6]}|{mines[7]}|")
    print(f"2|{mines[8]}|{mines[9]}|{mines[10]}|{mines[11]}|{mines[12]}|{mines[13]}|{mines[14]}|{mines[15]}|")
    print(f"3|{mines[16]}|{mines[17]}|{mines[18]}|{mines[19]}|{mines[20]}|{mines[21]}|{mines[22]}|{mines[23]}|")
    print(f"4|{mines[24]}|{mines[25]}|{mines[26]}|{mines[27]}|{mines[28]}|{mines[29]}|{mines[30]}|{mines[31]}|")
    print(f"5|{mines[32]}|{mines[33]}|{mines[34]}|{mines[35]}|{mines[36]}|{mines[37]}|{mines[38]}|{mines[39]}|")
    print(f"6|{mines[40]}|{mines[41]}|{mines[42]}|{mines[43]}|{mines[44]}|{mines[45]}|{mines[46]}|{mines[47]}|")
    print(f"7|{mines[48]}|{mines[49]}|{mines[50]}|{mines[51]}|{mines[52]}|{mines[53]}|{mines[54]}|{mines[55]}|")
    print(f"8|{mines[56]}|{mines[57]}|{mines[58]}|{mines[59]}|{mines[60]}|{mines[61]}|{mines[62]}|{mines[63]}|")
def player_move():
    while True:
        global move
        move = input("move (a1-h8F): ")
        if (move[0].isdigit() and move[1].isdigit() == False) or (((ord(move[0].lower()) - ord("a") + 1) < 1 or (ord(move[0].lower()) - ord("a") + 1) > 8) or (int(move[1]) < 1 or int(move[1]) > 8)):
            print_board()
            print("wrong move.")
            continue
        if move[len(move) - 1].lower() == "f":
            board_view[(ord(move[0].lower()) - ord("a") + 1) + 8 * (int(move[1]) - 1) - 1] = "F"
            return
        elif board[(ord(move[0].lower()) - ord("a") + 1) + 8 * (int(move[1]) - 1) - 1] == 9:
            print("lose")
            return False
        else:
            board_view[(ord(move[0].lower()) - ord("a") + 1) + 8 * (int(move[1]) - 1) - 1] = board[(ord(move[0].lower()) - ord("a") + 1) + 8 * (int(move[1]) - 1) - 1]
            return
def check_win():
    if "_" not in board_view and board[(ord(move[0].lower()) - ord("a") + 1) + 8 * (int(move[1]) - 1) - 1] != 9:
        print_board()
        print("win")
        return True
    else:
        return
while True:
    print_board()
    if player_move() == False:
        break
    if check_win():
        break