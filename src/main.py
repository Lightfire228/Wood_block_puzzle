
import board.board as board

from board.pieces import * 

def main():
    solved = board.start()

    if solved:
        print_solved()
    else:
        print_unsolved()

def print_solved():
    
    print('ITS RAINING MEN!!!!')

    positions = [POSITION_0, *POSITIONS]
    for position in positions:
        print_status(position)


def print_status(position):
    print(f'Position: {position.name}\tPiece: {position.piece.name}')


def print_unsolved():
    print('¯\_(ツ)_/¯')

if __name__ == "__main__":
    main()