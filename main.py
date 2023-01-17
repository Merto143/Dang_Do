from sys import argv
from codefiles.classes.car import Car
from codefiles.classes.board import Board
from codefiles.algorithms.algorithms import random_only_legal_moves_algorithm, random_all_moves_algorithm
import numpy as np
import random
from tqdm import tqdm


if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python3 main.py [filename]")
        exit(1)
    else:
        filename = argv[1]

    game = Board(6, filename)
    game.visual()
    all_moves = random_all_moves_algorithm(game)
    game = Board(6, filename)
    legal_moves = random_only_legal_moves_algorithm(game)

    print(f"All moves: {all_moves} try's to solve the problem")
    print(f"Legal moves: {legal_moves} try's to solve the problem")
    # all_iterations = []
    # for i in tqdm(range(100)):
    #     all_iterations.append(random_algorithm())
    #     game = Board(6, filename)
    #
    # print(all_iterations)
