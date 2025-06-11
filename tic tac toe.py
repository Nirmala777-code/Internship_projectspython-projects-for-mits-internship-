def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in zip(*board):
        if all(cell == player for cell in col):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell in ["X", "O"] for row in board for cell in row)

board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
current_player = "X"

while True:
    print_board(board)
    move = input(f"Player {current_player}, enter a number (1-9): ")

    valid = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == move:
                board[i][j] = current_player
                valid = True
                break
        if valid:
            break

    if not valid:
        print("❌ Invalid move. Try again.")
        continue

    if check_winner(board, current_player):
        print_board(board)
        print(f"🎉 Player {current_player} wins!")
        break
    elif is_draw(board):
        print_board(board)
        print("🤝 It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"