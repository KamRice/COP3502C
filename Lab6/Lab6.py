def initialize_board(num_rows, num_cols):
    new_board = []

    for row in range(1, num_rows + 1):
        column = []
        for col in range(1, num_cols + 1):
            column.append("-")
        new_board.append(column)
    return new_board


def print_board(_board):
    for member in range(len(_board) - 1, -1, -1):
        print(" ".join(_board[member]))


def insert_chip(_board, col, chip_type):
    if col not in range(0, len(_board[0])):
        return None

    for row in range(0, len(_board)):
        if _board[row][col] == "-":
            _board[row][col] = chip_type
            return [row, col]
    return None


def check_if_winner(_board, col, _row, chip_type):
    streak = 0
    # Row Check
    for _row in _board:
        streak = 0
        for spot in _row:
            if spot is chip_type:
                streak += 1
                if streak == 4:
                    return True
            else:
                streak = 0

    streak = 0

    # Column Check
    for column in range(0, len(_board[0])):
        streak = 0
        for _row in range(len(_board)):
            # print(f"Checking {_row},{column} : {_board[_row][column]}")
            if _board[_row][column] is chip_type:
                streak += 1
                if streak == 4:
                    return True
            else:
                streak = 0

    return False


if __name__ == "__main__":
    board = initialize_board(int(input("What would you like the height of the board to be?")),
                             int(input("What would you like the length of the board to be?")))
    print_board(board)
    print()
    print("Player 1: x", "Player 2: o", sep="\n")

    winner = False
    rows = len(board)
    columns = len(board[0])
    turn_count = 0

    while not winner:

        turn_count += 1
        if turn_count > rows * columns:
            winner = True
            print()
            print("Draw. Nobody wins.")
            break

        player1_move = insert_chip(board, int(input("\nPlayer 1: Which column would you like to choose?")), "x")
        print_board(board)
        if player1_move is not None:
            winner = check_if_winner(board, player1_move[0], player1_move[0], "x")
            if winner:
                print()
                print("Player 1 won the game!")
                break

        turn_count += 1
        if turn_count > rows * columns:
            winner = True
            print()
            print("Draw. Nobody wins.")
            break

        player2_move = insert_chip(board, int(input("\nPlayer 2: Which column would you like to choose?")), "o")
        print_board(board)
        if player2_move is not None:
            winner = check_if_winner(board, player2_move[0], player2_move[0], "o")
            if winner:
                print()
                print("Player 2 won the game!")
                break
