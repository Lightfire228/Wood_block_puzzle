import utilities
import rotation

from classes.piece    import Piece
from classes.point    import Point
from classes.position import Position

from constants import BOARD_SIZE
from constants import INSERTION_POINT


PIECE_00     = Piece('00',          '00.txt', BOARD_SIZE)
PIECE_06     = Piece('06',          '06.txt', BOARD_SIZE)
PIECE_06_INV = Piece('06 inverted', '06.txt', BOARD_SIZE, True)
PIECE_07     = Piece('07',          '07.txt', BOARD_SIZE)
PIECE_07_INV = Piece('07 inverted', '07.txt', BOARD_SIZE, True)
PIECE_08     = Piece('08',          '08.txt', BOARD_SIZE)
PIECE_08_INV = Piece('08 inverted', '08.txt', BOARD_SIZE, True)
PIECE_09     = Piece('09',          '09.txt', BOARD_SIZE)
PIECE_09_INV = Piece('09 inverted', '09.txt', BOARD_SIZE, True)
PIECE_10     = Piece('10',          '10.txt', BOARD_SIZE)
PIECE_10_INV = Piece('10 inverted', '10.txt', BOARD_SIZE, True)

# intentionally left out piece 00
PIECES = [
    PIECE_06, PIECE_06_INV,
    PIECE_07, PIECE_07_INV,
    PIECE_08, PIECE_08_INV,
    PIECE_09, PIECE_09_INV,
    PIECE_10, PIECE_10_INV,
]

# see `numerical_scheme.jpg` for an explanation of where these positions physically line up
POSITION_0 = Position('0', rotation.identity,           rotation.identity,           INSERTION_POINT)
POSITION_1 = Position('1', rotation.y_180,              rotation.identity,           INSERTION_POINT)
POSITION_2 = Position('2', rotation.z_counterclockwise, rotation.x_counterclockwise, INSERTION_POINT)
POSITION_3 = Position('3', rotation.z_counterclockwise, rotation.x_clockwise,        INSERTION_POINT)
POSITION_4 = Position('4', rotation.z_counterclockwise, rotation.y_counterclockwise, INSERTION_POINT)
POSITION_5 = Position('5', rotation.z_counterclockwise, rotation.y_clockwise,        INSERTION_POINT)

# intentionally left out
POSITIONS = [
    POSITION_1,
    POSITION_2,
    POSITION_3,
    POSITION_4,
    POSITION_5,
]
