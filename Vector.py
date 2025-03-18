import random
board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, 16):
    board[i] = random.randint(1, 4)
def print_board():
    print(board[0], board[1], board[2], board[3])
    print(board[4], board[5], board[6], board[7])
    print(board[8], board[9], board[10], board[11])
    print(board[12], board[13], board[14], board[15])
while True:
    print_board()
    while True:
        turn = int(input("Turn: "))
        if turn < 1 or turn > 16:
            print("Wrong turn.")
            print_board()
            continue
        if turn == 1:
            board[0] += 1
            board[1] += 1
            board[4] += 1
            board[5] += 1
        elif turn == 2 or turn == 3:
            board[turn - 2] += 1
            board[turn - 1] += 1
            board[turn] += 1
            board[turn + 2] += 1
            board[turn + 3] += 1
            board[turn + 4] += 1
        elif turn == 4:
            board[2] += 1
            board[3] += 1
            board[6] += 1
            board[7] += 1
        elif turn == 5 or turn == 9:
            board[turn - 5] += 1
            board[turn - 4] += 1
            board[turn - 1] += 1
            board[turn] += 1
            board[turn + 3] += 1
            board[turn + 4] += 1
        elif turn == 6 or turn == 7 or turn == 10 or turn == 11:
            for a in range(0, 3):
                for b in range(0, 3):
                    board[turn - 6 + b + 4 * a] += 1
        elif turn == 8 or turn == 12:
            board[turn - 6] += 1
            board[turn - 5] += 1
            board[turn - 2] += 1
            board[turn - 1] += 1
            board[turn + 2] += 1
            board[turn + 3] += 1
        elif turn == 13:
            board[8] += 1
            board[9] += 1
            board[12] += 1
            board[13] += 1
        elif turn == 14 or turn == 15:
            board[turn - 6] += 1
            board[turn - 5] += 1
            board[turn - 4] += 1
            board[turn - 2] += 1
            board[turn - 1] += 1
            board[turn] += 1
        elif turn == 16:
            board[10] += 1
            board[11] += 1
            board[14] += 1
            board[15] += 1
        for i in range(0, 16):
            if board[i] == 5:
                board[i] = 1
        break
    if 2 not in board and 3 not in board and 4 not in board:
        print_board()
        print("Win!")
        break