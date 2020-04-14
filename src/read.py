import utilities

from pathlib import Path

data_folder = Path(__file__).parent / '../data'

def read_block(file_name):
    
    file = _get_file(file_name)

    block = _parse_block_text(file.read_text())

    return block



def _get_file(file_name):
    block_folder = data_folder / 'blocks'

    return block_folder / file_name

def _parse_block_text(block_text):

    back  = []
    front = []

    for line in block_text.split('\n'):
        linesplit = line.split(' ')

        back .append(linesplit[0])
        front.append(linesplit[1])

    def parse(face):
        return [ 
            [ True if col == '#' else False for col in row ]
            for row in face 
        ]
    
    back  = parse(back)
    front = parse(front)

    return [back, front]


