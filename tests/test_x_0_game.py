
from x_0_game import winner
from x_0_game import display_board


def test__winner__who_is_win():
    board = ["X", "O", "X",
             "O", "O", "O",
             "O", "X", "X"]
    assert winner(board) == "O"


def test__winner__if_it_tie():
    board = ["X", "O", "X",
             "X", "O", "O",
             "O", "X", "X"]
    assert winner(board) == "TIE"


def test__display_board(capsys):
    board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    display_board(board)
    captured = capsys.readouterr()
    expected_output = '''
    X  | O | X    0  1  2
    ---+---+---
    O  | X | O    3  4  5
    ---+---+---
    X  | O | X    6  7  8
    '''
    assert captured.out.strip() == expected_output.strip()