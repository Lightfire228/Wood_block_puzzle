
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
                # str(r)
                (str(r) + ' ')[:5]
                for r in row
            ]) 
            for row in grid
        ]) 
        for grid in matrix 
    ])

if __name__ == "__main__":
    pass