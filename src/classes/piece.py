from classes.point import Point

import read
import utilities

class Piece():

    # size constants
    Z = 2
    Y = 6
    X = 2

    @staticmethod
    def get_dimensions():
        return Point(Piece.Z, Piece.Y, Piece.X)

    def __init__(self, piece_name, file_name, board_size, is_inverted=False):
        self.piece_name  = piece_name
        self.file_name   = file_name
        self.board_size  = board_size
        self.is_inverted = is_inverted

        self.piece_matrix = read.read_block(file_name)
        self.padded_matrix = self._get_padded_matrix()

    def _get_padded_matrix(self):

        blank_matrix = utilities.generate_3d_matrix(False, self.board_size)

        # hack away!
        for z in range(len(self.piece_matrix)):
            for y in range(len(self.piece_matrix[z])):
                for x in range(len(self.piece_matrix[z][y])):
                    blank_matrix[z][y][x] = self.piece_matrix[z][y][x]

    def _get_piece_matrix(self):

        piece_matrix = read.read_block(self.file_name)

        #TODO:
        # if self.is_inverted:
        #     piece_matrix = rotation.rotate_3d_matrix(rotation.z_)


