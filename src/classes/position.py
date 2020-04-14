import utilities
import rotation
import read

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
        rotated_point = rotation.apply_point_rotation(self.rotation_matrix2, rotated_point, center=center)


        return rotated_point

    def set_piece(self, piece):
        self.piece = piece
