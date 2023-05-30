import pytest

from test_x_0_game import winner
from test_x_0_game import display_board


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


def test__winner__if_no_win():
    board = ["X", "O", "X",
             "X", "O", "O",
             "O", "X", "O"]
    assert winner(board) == None

def test__display_board:
    pass

