import utilities

from utilities import Point

identity = [
    [ 1,  0,  0],
    [ 0,  1,  0],
    [ 0,  0,  1],
]

## 
# Because everything is [z, y, x], I didn't want to swap the arguments around
# in the multiplication function.  So, instead, I name the mathematical x-axis
# rotation matrices as z-axis rotation matrices and vise-versa.  So, in effect,
# the `z_clockwise` will still rotate about the z-axis, if you look up the rotation
# matrix definitions, they'll be swapped

#         # the x-rotation matrix                     
#                                                     
#          [1,       0,      0]   [z]  # the inverted    
#  Rz(θ) = |0,  cos(θ), sin(θ)| * |y|  # position vector 
#          [0, -sin(θ), cos(θ)]   [x]                    
#                                                     


# mathematically the x-clockwise
z_clockwise = [
    [ 1,  0,  0],
    [ 0,  0, -1],
    [ 0,  1,  0],
]

# mathematically the x-counterclockwise
z_counterclockwise = [
    [ 1,  0,  0],
    [ 0,  0,  1],
    [ 0, -1,  0],
]

# mathematically the x-180
z_180 = [
    [ 1,  0,  0],
    [ 0, -1,  0],
    [ 0,  0, -1],
]

y_clockwise = [
    [ 0,  0,  1], 
    [ 0,  1,  0], 
    [-1,  0,  0], 
]

y_counterclockwise = [
    [ 0,  0, -1], 
    [ 0,  1,  0], 
    [ 1,  0,  0], 
]

y_180 = [
    [-1,  0,  0], 
    [ 0,  1,  0], 
    [ 0,  0, -1], 
]

# mathematically the z-counterclockwise
x_clockwise = [
    [ 0, -1,  0], 
    [ 1,  0,  0], 
    [ 0,  0,  1], 
]

# mathematically the z-counterclockwise
x_counterclockwise = [
    [ 0,  1,  0], 
    [-1,  0,  0], 
    [ 0,  0,  1], 
]


def apply_point_rotation(rotation_matrix, point, center=Point.ZERO):

    translated_point = point.translate(center, True)

    point_matrix = utilities.convert_to_vertical_matrix(translated_point.to_vector())

    rotated_matrix = utilities.matrix_multiplication(rotation_matrix, point_matrix)

    rotated_vector = utilities.convert_to_array(rotated_matrix)

    return Point(*rotated_vector).translate(center)


def rotate_3d_matrix(rotation_matrix, matrix, center=None):
    """
        center defaults to the center of the 3d matrix
    """

    
    z_len = len(matrix)
    y_len = len(matrix[0])
    x_len = len(matrix[0][0])

    if center == None:
        center = Point(
            (z_len -1 ) / 2,
            (y_len -1 ) / 2,
            (x_len -1 ) / 2,
        )

    result = [
        [
            [
                -2
                for z in y
            ]
            for y in z
        ]
        for z in matrix
    ]

    for z in range(z_len):
        for y in range(y_len):
            for x in range(x_len):

                mapped_point = apply_point_rotation(rotation_matrix, Point(z, y, x), center)
                
                mZ = int(mapped_point.Z)
                mY = int(mapped_point.Y)
                mX = int(mapped_point.X)

                result[z][y][x] = matrix[mZ][mY][mX]

    return result



def _gen_test_matrix(size):

    t = utilities.generate_3d_matrix(-1, size)

    for i in range(size**3):
        z = (i // size) // size
        y = (i // size)  % size
        x = i % size

        t[z][y][x] = i
    
    return t

def test():

    size = 2

    t = _gen_test_matrix(size)

    print('OG ===>')
    print(utilities.to_string_3d_matrix(t))

    r = rotate_3d_matrix(identity, t)

    print('\nNEW ###>')
    print(utilities.to_string_3d_matrix(r))

if __name__ == "__main__":
    test()
