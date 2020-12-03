import argparse
import os
from pathlib import Path

FIRST_BYTE_POSITION = 0
BUFFER_SIZE = 1024


def generate_reversed_file(input_file_path: Path) -> Path:
    output_file_path = input_file_path.parent / f'{input_file_path.stem}_output{input_file_path.suffix}'
    file_size = input_file_path.stat().st_size
    bytes_to_read = BUFFER_SIZE if BUFFER_SIZE < file_size else file_size
    index = -bytes_to_read

    with input_file_path.open('rb') as input_file, output_file_path.open('wb') as output_file:
        input_file.seek(index, os.SEEK_END)

        while True:
            current_position = input_file.tell()

            byte = input_file.read(bytes_to_read)
            reversed_bytes = byte[::-1]
            output_file.write(reversed_bytes)

            if current_position == FIRST_BYTE_POSITION:
                break

            if current_position < BUFFER_SIZE:
                bytes_to_read = current_position

            index -= bytes_to_read
            input_file.seek(index, os.SEEK_END)

    return output_file_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_files', nargs='+', type=Path)

    args = parser.parse_args()

    for f in args.input_files:
        generate_reversed_file(f)
