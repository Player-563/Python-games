board = ["_", "_", "_", "_", "_", "_", " ", " ", " "]
player = ""
def print_board():
	print(f"{board[0]}|{board[1]}|{board[2]}")
	print(f"{board[3]}|{board[4]}|{board[5]}")
	print(f"{board[6]}|{board[7]}|{board[8]}")
def draw_check():
	if "_" not in board and " " not in board:
		print_board()
		print("It's a draw!")
		return True
	else:
		return False
def win_check(player):
	if board[0] == board[1] == board[2] == player or board[3] == board[4] == board[5] == player or board[6] == board[7] == board[8] == player or board[0] == board[3] == board[6] == player or board[1] == board[4] == board[7] == player or board[2] == board[5] == board[8] == player or board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
		print_board()
		print(f"{player} win!")
		return True
	else:
		return False
def turn(player):
	while True:
		move = int(input(f"{player} turn: "))
		if move >= 1 and move <= 9:
			if board[move - 1] == "_" or board[move - 1] == " ":
				board[move - 1] = player
			else:
				print("This cell is occupied!")
				print_board()
				continue
		else:
			print("Wrong move!")
			print_board()
			continue
		break
def game_loop():
	while True:
		print_board()
		player = "X"
		turn(player)
		if win_check(player):
			return
		if draw_check():
			return
		while True:
			print_board()
			player = "O"
			turn(player)
			if win_check(player):
				return
			if draw_check():
				return
			break
game_loop()