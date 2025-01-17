from classes.point import Point
from constants     import BOARD_CENTER

import utilities

def identity(point):
    return point

def z_counterclockwise(point):
    return Point(
        point.Z,
        -point.X,
        point.Y,
    )

def z_clockwise(point):
    return Point(
        point.Z,
        point.X,
        -point.Y,
    )

def z_180(point):
    return Point(
        point.Z,
        -point.Y,
        -point.X,
    )

def y_counterclockwise(point):
    return Point(
        point.X,
        point.Y,
        -point.Z,
    )

def y_clockwise(point):
    return Point(
        -point.X,
        point.Y,
        point.Z,
    )

def y_180(point):
    return Point(
        -point.Z,
        point.Y,
        -point.X,
    )


def x_counterclockwise(point):
    return Point(
        -point.Y,
        point.Z,
        point.X
    )

def x_clockwise(point):
    return Point(
        point.Y,
        -point.Z,
        point.X
    )

def apply_point_rotation(rotation, point, center=None):

    center = BOARD_CENTER if center == None else center

    centered_point = point.translate(center, True)
    rotated_point  = rotation(centered_point)

    return rotated_point.translate(center).to_int_point()

def rotate_3d_matrix(rotation_matrix, matrix, center=None):
    
    z_len = len(matrix)
    y_len = len(matrix[0])
    x_len = len(matrix[0][0])

    result = [
        [
            [
                0
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

                mZ = mapped_point.Z
                mY = mapped_point.Y
                mX = mapped_point.X

                result[mZ][mY][mX] = matrix[z][y][x]

    return result

def _gen_test_matrix(size):

    t = utilities.generate_3d_matrix(0, size)

    for i in range(size**3):
        z = (i // size) // size
        y = (i // size)  % size
        x = i % size

        t[z][y][x] = i
    
    return t

def test():

    size = 6

    t = _gen_test_matrix(size)

    print(f'>>>>>>>>>>>> OG ===>')
    print(utilities.to_string_3d_matrix(t))

    r = rotate_3d_matrix(z_counterclockwise, t)

    print(f'>>>>>>>>>>>> \nNEW ###>')
    print(utilities.to_string_3d_matrix(r))

if __name__ == "__main__":
    test()
