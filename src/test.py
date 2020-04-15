from constants    import *
from board.pieces import *

def main():
    test_position_rotations()

def test_position_rotations():

    p = POSITION_5

    print(f'>>>>>>>>>>>> p5 origin {p.origin}')
    print(f'>>>>>>>>>>>> p5 dim    {p.dimensions}')


if __name__ == "__main__":
    main()