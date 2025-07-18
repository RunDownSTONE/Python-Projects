import random

def print_board(board):
    print("\nCurrent Board:")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_valid_input(prompt, valid_range):
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            print(f"Invalid input. Please enter {' or '.join(str(x) for x in valid_range)}")
        except ValueError:
            print("Please enter a number")

def computer_move(board):
    # Check for winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if check_winner(board) == "O":
                    board[i][j] = " "
                    return (i, j)
                board[i][j] = " "
    
    # Block opponent's winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if check_winner(board) == "X":
                    board[i][j] = " "
                    return (i, j)
                board[i][j] = " "
    
    # Choose a random available spot
    empty_spots = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_spots)

def play_game(mode):
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    is_computer = mode == 1  # Computer is "O"

    while True:
        print_board(board)
        
        if is_computer and current_player == "O":
            print("\nComputer's turn (O)...")
            row, col = computer_move(board)
        else:
            print(f"\nPlayer {current_player}'s turn")
            row = get_valid_input("Enter row (0-2): ", [0, 1, 2])
            col = get_valid_input("Enter column (0-2): ", [0, 1, 2])

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            if not is_computer or current_player != "O":
                print("Position already taken! Try again.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "O" and is_computer:
                print("\nComputer wins!")
            else:
                print(f"\nPlayer {winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("\nIt's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

def main():
    print("Welcome to Tic-Tac-Toe!")
    print("\nGame Modes:")
    print("1. Player vs Computer")
    print("2. Player vs Player")
    
    while True:
        try:
            mode = int(input("\nSelect game mode (1 or 2): "))
            if mode in [1, 2]:
                break
            print("Please enter 1 or 2")
        except ValueError:
            print("Please enter a number")
    
    print("\nGame Starting...")
    print("X always goes first")
    print("When selecting positions:")
    print("- First number is row (0-2)")
    print("- Second number is column (0-2)")
    print("\nExample: Row 0, Column 2 is top-right corner\n")
    
    play_game(mode)
    
    while True:
        replay = input("\nPlay again? (y/n): ").lower()
        if replay == 'y':
            play_game(mode)
            break
        elif replay == 'n':
            print("\nThanks for playing!")
            break
        else:
            print("Please enter 'y' or 'n'")

if __name__ == "__main__":
    main()
