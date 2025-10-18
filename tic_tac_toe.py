
"""
Simple Tic-Tac-Toe game written in a beginner style.
Asks for two player names and alternates turns until someone wins or it's a draw.
"""

def print_board(board):
    print()
    for i in range(3):
        row = ' | '.join(board[i*3:(i+1)*3])
        print(' ' + row)
        if i < 2:
            print('---+---+---')
    print()

def check_winner(board, mark):
    # rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == mark:
            return True
    # cols
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == mark:
            return True
    # diagonals
    if board[0] == board[4] == board[8] == mark:
        return True
    if board[2] == board[4] == board[6] == mark:
        return True
    return False

def is_draw(board):
    return all(cell != ' ' for cell in board)

def get_move(player_name, board):
    while True:
        try:
            move = input(f"{player_name}, enter your move (1-9): ")
            pos = int(move) - 1
            if pos < 0 or pos > 8:
                print("Invalid position. Choose a number from 1 to 9.")
                continue
            if board[pos] != ' ':
                print("That spot is already taken. Choose another.")
                continue
            return pos
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Welcome to Tic-Tac-Toe!")
    p1 = input("Enter name for Player 1 (X): ") or "Player1"
    p2 = input("Enter name for Player 2 (O): ") or "Player2"
    players = [(p1, 'X'), (p2, 'O')]

    board = [' '] * 9
    current = 0

    while True:
        print_board(board)
        name, mark = players[current]
        pos = get_move(name, board)
        board[pos] = mark

        if check_winner(board, mark):
            print_board(board)
            print(f"Congratulations {name}! You have won the game.")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current = 1 - current

    print("Game over. Thanks for playing!")

if __name__ == '__main__':
    main()
