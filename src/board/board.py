from constants    import *
from board.pieces import *

from classes.point    import Point
from classes.piece    import Piece
from classes.position import Position

import rotation
import utilities

def start():

    board = utilities.generate_3d_matrix(False, BOARD_SIZE)

def insert_piece(board_matrix, piece, position):

    position.set_piece(piece)

    rotated_piece_matrix = position.apply_matrix_rotations(piece)

    for point in walk_position_indices(position):
        board_matrix[point.Z][point.Y][point.X] = rotated_piece_matrix[point.Z][point.Y][point.X]


def check_collides(board_matrix, piece, position):

    rotated_piece_matrix = position.apply_matrix_rotations(piece)

    for point in walk_position_indices(position):

        board_value = board_matrix        [point.Z][point.Y][point.X]
        piece_value = rotated_piece_matrix[point.Z][point.Y][point.X]

        if board_value and piece_value:
            return True
    
    return False


def walk_position_indices(position):
    origin = position.origin
    dim    = position.dimensions

    z_range = _get_range(origin.Z, dim.Z)
    y_range = _get_range(origin.Y, dim.Y)
    x_range = _get_range(origin.X, dim.X)

    for z in z_range:
        for y in y_range:
            for x in x_range:
                yield Point(z, y, x)


def _get_range(origin, dim):

    return range(origin, (origin + dim), -1 if dim < 0 else 1)

