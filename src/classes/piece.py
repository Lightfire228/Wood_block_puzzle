from classes.point import Point

from constants import PIECE_CENTER
from constants import INSERTION_POINT

import read
import utilities
import rotation

class Piece():

    DIMENSIONS = Point(
        2,
        6,
        2,
    )

    @staticmethod
    def get_dimensions():
        return Point(Piece.Z, Piece.Y, Piece.X)

    def __init__(self, piece_name, file_name, board_size, is_inverted=False):
        self.piece_name  = piece_name
        self.file_name   = file_name
        self.board_size  = board_size
        self.is_inverted = is_inverted

        self.piece_matrix  = self._get_piece_matrix()
        self.padded_matrix = self._get_padded_matrix()

    def _get_padded_matrix(self):

        blank_matrix = utilities.generate_3d_matrix(False, self.board_size)

        dim   = Piece.DIMENSIONS
        start = INSERTION_POINT

        # hack away!
        for z in range(dim.Z):
            for y in range(dim.Y):
                for x in range(dim.X):

                    z_board = start.Z + z
                    y_board = start.Y + y
                    x_board = start.X + x

                    blank_matrix[z_board][y_board][x_board] = self.piece_matrix[z][y][x]

        return blank_matrix

    def _get_piece_matrix(self):

        piece_matrix = read.read_block(self.file_name)

        if self.is_inverted:
            piece_matrix = rotation.rotate_3d_matrix(rotation.z_180, piece_matrix, PIECE_CENTER)
        
        return piece_matrix
        



