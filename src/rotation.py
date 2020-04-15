from classes.point import Point

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

#region test
def apply_point_rotation(rotation, point, center=Point.ZERO):
    centered_point = point.translate(center, True)
    rotated_point  = rotation(centered_point)

    return rotated_point.translate(center)



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
                
                mZ = int(mapped_point.Z)
                mY = int(mapped_point.Y)
                mX = int(mapped_point.X)

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
#endregion
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
