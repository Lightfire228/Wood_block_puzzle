from constants    import *
from board.pieces import *

import board.board as board

import utilities

def main():
    # test_position_rotations()
    # test_piece_inversion()
    # test_walk()
    # test_board_insertion()
    test_collide()

def test_position_rotations():

    p = POSITION_5

    print(f'>>>>>>>>>>>> p5 origin {p.origin}')
    print(f'>>>>>>>>>>>> p5 dim    {p.dimensions}')

def test_piece_inversion():
    p     = PIECE_06
    p_inv = PIECE_06_INV

    print(f'>>>>>>>>>>>> p')
    print(utilities.to_string_3d_matrix(p.piece_matrix))

    print(f'\n>>>>>>>>>>>> p_inv')
    print(utilities.to_string_3d_matrix(p_inv.piece_matrix))

def test_walk():

    p   = PIECE_06
    pos = POSITION_5

    board.walk_piece_matrix(p, pos)

def test_board_insertion():
    board_matrix = utilities.generate_3d_matrix(False, 6)

    rotated_matrix = POSITION_5.apply_matrix_rotations(PIECE_06)
    print(f'>>>>>>>>>>>> rotated matrix')
    print(utilities.to_string_3d_matrix(rotated_matrix))


def test_collide():
    board_matrix = utilities.generate_3d_matrix(False, 6)

    board.insert_piece(board_matrix, PIECE_00, POSITION_0)
    print(f'>>>>>>>>>>>> board yes collide:', board.check_collides(board_matrix, PIECE_06, POSITION_5))

    board.insert_piece(board_matrix, PIECE_00, POSITION_0)
    print(f'>>>>>>>>>>>> board no collide:', board.check_collides(board_matrix, PIECE_06_INV, POSITION_5))

if __name__ == "__main__":
    main()