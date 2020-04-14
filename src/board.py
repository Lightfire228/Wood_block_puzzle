from constants import *

from classes.point    import Point
from classes.piece    import Piece
from classes.position import Position

import rotation
import utilities

print(f'>>>>>>>>>>>> s {Point}')

def start():

    board = utilities.generate_3d_matrix(False, BOARD_SIZE)

def insert_piece(board, piece, position):

    dimensions = Piece.get_dimensions()

    rotated_dim = position.apply_point_rotations(dimensions, Point.ZERO).abs()
    # offset      = position.

    # for z in 

