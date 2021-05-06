from typing import Literal
import os


def convert_unit(unit: Literal['B', 'KB', 'MB', 'GB']):
    "Decorator: Returns converted result from byte"

    # TODO: Complete here
    def type_convert_unit(func):
        def inner(*args, **kwargs):
            size_byte = func(*args)
            if unit == 'KB':
                return size_byte // 1024
            if unit == 'MB':
                return size_byte // (1024 * 1024)
            if unit == 'GB':
                return size_byte // (1024 * 1024 * 1024)

        return inner

    return type_convert_unit


@convert_unit('KB')
def get_directory_size(directory: str) -> int:
    size = []
    for root, dirs, files in os.walk(directory, topdown=True):
        for file in files:
            addres = f"{root}/{file}"
            size.append(os.path.getsize(addres))

    return sum(size)


# print(get_directory_size('/home/sasanpy/Downloads/'))

if __name__ == '__main__':
    print(os.getcwd())
    print(get_directory_size(os.getcwd()))
