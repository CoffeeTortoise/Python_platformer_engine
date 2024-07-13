from random import randint
from sys import exit


class Error:
    """The joke error class"""
    def __init__(self):
        n = randint(0, 6)
        if n == 1:
            print(f'Unexpected error: {self}')
            print('Not enough coffee to continue!')
            print('Process terminated with exit status 1')
            exit(1)

    def __del__(self):
        pass
