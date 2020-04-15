from constants    import *
from board.pieces import *

import utilities

def main():
    # test_position_rotations()
    test_piece_inversion()

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


if __name__ == "__main__":
    main()