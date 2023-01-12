from typing import Any, List
from sys import argv
from car import Car
from board import Board


if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python3 RushHour.py [filename]")
        exit(1)
    else:
        filename = argv[1]

    grid = Board(6, filename)
