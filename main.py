from sys import argv
from codefiles.classes.car import Car
from codefiles.classes.board import Board
from codefiles.algorithms.algorithms import random_only_legal_moves_algorithm, random_all_moves_algorithm


if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python3 main.py [filename]")
        exit(1)
    else:
        filename = argv[1]
        dimension = int(filename[8])

    game = Board(dimension, filename)
    game.visual()
    all_moves = random_all_moves_algorithm(game)
    game = Board(dimension, filename)
    legal_moves = random_only_legal_moves_algorithm(game)

    print(f"All moves: {all_moves} try's to solve the problem")
    print(f"Legal moves: {legal_moves} try's to solve the problem")
    # all_iterations = []
    # for i in tqdm(range(100)):
    #     all_iterations.append(random_algorithm())
    #     game = Board(6, filename)
    #
    # print(all_iterations)
