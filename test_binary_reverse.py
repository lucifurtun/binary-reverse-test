import binascii
import os
from pathlib import Path

from binary_reverse import generate_reversed_file

BYTES = [
    b'20', b'c7', b'57', b'6d', b'5d', b'10', b'fb', b'8c', b'd4', b'ab', b'f6', b'9d', b'50', b'49', b'00', b'4f',
    b'29', b'4d', b'99', b'b9', b'7b', b'3d', b'67', b'f2', b'af', b'90', b'0a', b'e0', b'57', b'b5', b'68', b'98',
    b'6d', b'c1', b'23', b'd5', b'04', b'61', b'3a', b'52', b'de', b'9b', b'ca', b'26', b'37', b'0b', b'86', b'97',
    b'a9', b'cb', b'0e', b'60', b'6f', b'97', b'0d', b'c7', b'30', b'12', b'44', b'ed', b'1d', b'12', b'f2', b'86'
]


def test_generate_reversed_file(tmp_path: Path):
    test_file = tmp_path / 'some_file.bin'

    content = binascii.unhexlify(b''.join(BYTES))
    reversed_content = content[::-1]

    with test_file.open('wb') as f:
        f.write(content)

    output_file_path = generate_reversed_file(test_file)

    with output_file_path.open('rb') as output_file:
        output_data = output_file.read()

    assert output_file_path.exists()
    assert output_data == reversed_content


def test_generate_reversed_file_large_file(tmp_path: Path):
    file_size_in_mb = 100
    test_file = tmp_path / 'some_file.bin'

    content = os.urandom(file_size_in_mb * (10 ** 6))
    reversed_content = content[::-1]

    with test_file.open('wb') as f:
        f.write(content)

    output_file_path = generate_reversed_file(test_file)

    with output_file_path.open('rb') as output_file:
        output_data = output_file.read()

    assert output_file_path.exists()
    assert output_data == reversed_content
