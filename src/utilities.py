
def generate_3d_matrix(value, size):
    return [generate_2d_matrix(value, size) for i in range(size)]

def generate_2d_matrix(value, size):
    return [generate_matrix(value, size) for i in range(size)]

def generate_matrix(value, size):
    return [value] * size

def to_string_3d_matrix(matrix):

    def s_row (r): return ' '.join(r)
    def s_grid(g): return '\n'.join(g)
    def s_cube(c): return '\n=======\n'.join(c)

    return s_cube([
        s_grid([
            s_row([
                str(r) 
                for r in row
            ]) 
            for row in grid
        ]) 
        for grid in matrix 
    ])

def convert_to_vertical_matrix(array):
    return [
        [x]
        for x in array
    ]

def convert_to_array(matrix):
    return [x[0] for x in matrix]

def matrix_multiplication(a, b):

    a_height = len(a)
    a_width  = len(a[0])
    b_height = len(b)
    b_width  = len(b[0])

    r_height = a_height
    r_width  = b_width

    if a_width != b_height:
        raise Exception(f'Matrix a\'s width must be the same as matrix b\'s height: values {len(a[0])} and {len(b)}')

    result = [generate_matrix(0, r_width) for i in range(r_height)]

    for r_y in range(r_height):
        for r_x in range(r_width):

            product = 0
            for i in range(a_width):
                product += a[r_y][i] * b[i][r_x]
            
            result[r_y][r_x] = product
    
    return result


class Point():

    def __init__(self, z, y, x):
        self.Z = z
        self.Y = y
        self.X = x

    def to_vector(self):
        return [self.Z, self.Y, self.X]

    def translate(self, point, subtract=False):

        inv = -1 if subtract else 1

        new_Z = self.Z + (point.Z * inv)
        new_Y = self.Y + (point.Y * inv)
        new_X = self.X + (point.X * inv)

        return Point(new_Z, new_Y, new_X)

    def abs(self):
        return Point(
            abs(self.Z),
            abs(self.Y),
            abs(self.X),
        )

    def __str__(self):
        return f'({self.Z}, {self.Y}, {self.X})'

    def __eq__(self, value):
        return isinstance(value, Point) \
            and value.Z == self.Z       \
            and value.Y == self.Y       \
            and value.X == self.X
    
    def __ne__(self, value):
         return not self.__eq__(value)

# python be weird
# https://stackoverflow.com/a/2546626/2716305
Point.ZERO = Point(0, 0, 0)

if __name__ == "__main__":

    a = [
        [1, 2, 3], 
        [4, 5, 6],
    ]

    b = [
        [ 7,  8], 
        [ 9, 10],
        [11, 12]
    ]

    product = matrix_multiplication(a, b)

    print(to_string_3d_matrix([product]))