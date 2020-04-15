import utilities
import rotation
import read

class Position():
    
    def __init__(self, name, rotation_matrix1, rotation_matrix2, insertion_point):

        self.name             = name
        self.rotation_matrix1 = rotation_matrix1
        self.rotation_matrix2 = rotation_matrix2

        self.origin = self.apply_point_rotations(insertion_point)

    def apply_matrix_rotations(self, piece):
        
        matrix = piece.padded_matrix

        matrix = rotation.rotate_3d_matrix(self.rotation_matrix1, matrix)
        matrix = rotation.rotate_3d_matrix(self.rotation_matrix2, matrix)

        return matrix

    def apply_point_rotations(self, point):

        rotated_point = point
        rotated_point = rotation.apply_point_rotation(self.rotation_matrix1, rotated_point)
        rotated_point = rotation.apply_point_rotation(self.rotation_matrix2, rotated_point)


        return rotated_point

    def set_piece(self, piece):
        self.piece = piece
