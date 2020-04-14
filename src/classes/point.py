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

print(f'>>>>>>>>>>>> {Point.ZERO}')