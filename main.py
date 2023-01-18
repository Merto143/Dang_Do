from sys import argv
from codefiles.classes.car import Car
from codefiles.classes.board import Board
from codefiles.algorithms.algorithms import random_only_legal_moves_algorithm, random_all_moves_algorithm, breadth_first
from tqdm import tqdm


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 main.py [filename]")
        exit(1)
    else:
        filename = argv[1]

        if filename[9] == "2":
            dimension = 12
        else:
            dimension = int(filename[8])

    nr = 100
    results = []
    game = Board(dimension, filename)
    breadth_first(game)

    # for i in tqdm(range(nr)):
    #     game = Board(dimension, filename)
    #     legal_moves = random_only_legal_moves_algorithm(game)
    #     results.append(legal_moves)
    #
    # print(f"{nr} iterations: the lowest number for legal moves is {min(results)} moves.")


# dit is wat we hiervoor gebruikten om het een enkele keer te laten runnen
    # game = Board(dimension, filename)
    # game.visual()
    # all_moves = random_all_moves_algorithm(game)
    # game = Board(dimension, filename)
    # legal_moves = random_only_legal_moves_algorithm(game)
    #
    # print(f"All moves: {all_moves} try's to solve the problem")
    # print(f"Legal moves: {legal_moves} try's to solve the problem")
