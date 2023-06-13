from game import display_instruct, who_goes_first, new_board, display_board, winner, human_move, computer_move, next_turn, get_congrat_message

X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9
COMP_VARIANTS = (0, 1, 2, 3, 4, 5, 6, 7, 8)

def main() -> None:
    display_instruct()
    computer, human = who_goes_first()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        print(display_board(board))
        turn = next_turn(turn)

    the_winner = winner(board)
    congrats_message = get_congrat_message(the_winner, computer, human)
    print(congrats_message)

if __name__ == '__main__':
    main()