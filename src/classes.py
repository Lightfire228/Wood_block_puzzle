import utilities
import rotation
import read

from utilities import Point

class Position():
    
    def __init__(self, name, rotation_matrix1, rotation_matrix2, insertion_point, board_center):

        self.name             = name
        self.rotation_matrix1 = rotation_matrix1
        self.rotation_matrix2 = rotation_matrix2
        self.board_center     = board_center

        self.origin = self.apply_point_rotations(insertion_point, center=board_center)

    def apply_matrix_rotations(self, piece):
        
        matrix = piece.padded_matrix

        matrix = rotation.rotate_3d_matrix(self.rotation_matrix1, matrix, self.board_center)
        matrix = rotation.rotate_3d_matrix(self.rotation_matrix2, matrix, self.board_center)

        return matrix

    def apply_point_rotations(self, point, center=None):
        center = self.board_center if center == None else center

        rotated_point = point
        rotated_point = rotation.apply_point_rotation(self.rotation_matrix1, rotated_point, center=center)
        print ('test 1', rotated_point)
        rotated_point = rotation.apply_point_rotation(self.rotation_matrix2, rotated_point, center=center)


        return rotated_point

    def set_piece(self, piece):
        self.piece = piece


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


