import random
import time
from typing import Optional


X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9
COMP_VARIANTS = (0, 1, 2, 3, 4, 5, 6, 7, 8)


def say(message: str, wait_sec: int) -> None:
    wait_sec = random.randint(1, 3)
    time.sleep(wait_sec)
    print(message)


def display_instruct() -> None:
    say(
        """
        Welcome to the greatest Russian game 'Крестики-Нолики'""", 2)


    say("""You will make your move known by entering a number, 0 - 8.""", 2)

    say("""The number will correspond to the board position as illustrated:""", 1)

    print("""
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8
    """
    )


def ask_number(question: str, low: int, high: int) -> int | None:
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return response


def who_goes_first() -> tuple[str, str]:
    go_first = random.randint(0, 1)
    if go_first == 0:
        print("\nTake the first move.")
        human = X
        computer = O
    else:
        print("\nComputer goes first.")
        computer = X
        human = O
    return computer, human


def new_board() -> list:
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board: list[str]) -> str:
    board_string = f'''
    {board[0]}  | {board[1]} | {board[2]}    0  1  2
    ---+---+---
    {board[3]}  | {board[4]} | {board[5]}    3  4  5
    ---+---+---
    {board[6]}  | {board[7]} | {board[8]}    6  7  8
    '''
    return board_string


def get_legal_moves(board: list[str]) -> list[int]:
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board: list[str]) -> str | None:
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None


def human_move(board: list[str], human: str) -> int:
    legal = get_legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied. Choose another one.\n")
    print("Fine...")
    assert move is not None
    return move


def computer_move(board: list[str], computer: str, human: str) -> int:
    board = board[:]
    comp_moves = random.sample(COMP_VARIANTS, 9)
    say('', 1)
    say("Computer takes number,", 2)
    for move in get_legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    for move in get_legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in comp_moves:
        if move in get_legal_moves(board):
            print(move)
            return move
    raise AssertionError('function does not go to this place')

def next_turn(turn: str) -> str:
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner: Optional[str], computer: str, human:str) -> None:
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == computer:
        print("Computer won.\n")

    elif the_winner == human:
        print("Congratulations. You won!\n") 
