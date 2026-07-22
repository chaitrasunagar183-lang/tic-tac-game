# Simple Terminal Tic-Tac-Toe
# Players: X and O
# Type 'q' anytime to quit the game.

def print_board(board):
    print("\nCurrent Board:")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def check_winner(board):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c]:
            return board[a]

    return None


def board_full(board):
    return all(cell in ("X", "O") for cell in board)


# Initial board
board = [str(i) for i in range(1, 10)]
current_player = "X"

print("=" * 35)
print("      TIC - TAC - TOE")
print("=" * 35)
print("Choose a position from 1 to 9.")
print("Type 'q' anytime to quit.\n")

print_board(board)

while True:
    move = input(f"Player {current_player}, enter your move (1-9) or q: ").strip()

    # Quit game
    if move.lower() == "q":
        print("\nGame Quit. Thanks for playing! 👋")
        break

    # Validate input
    if not move.isdigit():
        print("Please enter a number between 1 and 9.")
        continue

    position = int(move)

    if position < 1 or position > 9:
        print("Position must be between 1 and 9.")
        continue

    index = position - 1

    if board[index] in ("X", "O"):
        print("That position is already taken. Try another one.")
        continue

    # Make move
    board[index] = current_player

    # Show current board after every move
    print_board(board)

    # Check winner
    winner = check_winner(board)
    if winner:
        print(f"🎉🔥 Congratulations! Winner is '{winner}' 🔥🎉")
        break

    # Check draw
    if board_full(board):
        print("🤝 It's a Draw!")
        break

    # Switch player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"