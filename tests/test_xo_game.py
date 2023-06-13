from xo_game.game import display_board, get_legal_moves, next_turn, winner
import pytest


@pytest.mark.parametrize("board, expected_winner", [
    pytest.param(["X", "X", "X",
      "O", "O", " ",
      " ", " ", " "], "X", id='X fon'),
    (["O", "O", " ",
      "X", "X", "X",
      " ", " ", " "], "X"),
    (["X", "O", "X",
      "O", "O", "X",
      "X", "X", "O"], "TIE"),
    (["O", "O", "O",
      "X", "X", " ",
      "O", "X", " "], "O"),
])
def test__winner(board, expected_winner):
    assert winner(board) == expected_winner



def test__display_board():
    board = ["X", "O", "X", "O", "O", " ", " ", " ", " "]
    expected_output = """
    X  | O | X    0  1  2
    ---+---+---
    O  | O |      3  4  5
    ---+---+---
       |   |      6  7  8
    """

    actual_output = display_board(board)
    assert actual_output.strip() == expected_output.strip()


@pytest.mark.parametrize(
    'moves, expected_moves',
    [
        (["X", "O", "X", "O", "O", " ", " ", " ", " "], [5, 6, 7, 8]),
        ([" ", " ", " ", "O", "O", " ", " ", "X", "X"], [0, 1, 2, 5, 6]),
        ([" ", " ", " ", " ", "O", " ", " ", " ", "X"], [0, 1, 2, 3, 5, 6, 7]),
    ]
)
def test__get_legal_moves(moves, expected_moves):
    assert get_legal_moves(moves) == expected_moves

def test__next_turn():
    assert next_turn("X") == "O"
    assert next_turn("O") == "X"


