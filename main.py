from sys import argv
from codefiles.classes.car import Car
from codefiles.classes.board import Board
from codefiles.visualisations.visuals import *
from codefiles.algorithms.algorithms import random_only_legal_moves_algorithm, random_all_moves_algorithm
from codefiles.algorithms.algorithms import breadth_first
# from codefiles.algorithms.depth_first import DepthFirst
# =======
from codefiles.algorithms.algorithms import breadth_first
from codefiles.algorithms.algorithms import breadth_first
# from codefiles.algorithms.depth_first import DepthFirst
from codefiles.algorithms.breadth_first import BreadthFirst
from codefiles.algorithms.breadth_first_random_states import BreadthFirstRandomStates

from tqdm import tqdm
import time



if __name__ == "__main__":
    if len(argv) != 3 and len(argv) != 4:
        print("Usage: python3 main.py [filename] [algorithm] OR python3 main.py statistics [algorithm] [dimension]")
        exit(1)

    elif len(argv) == 3:
        filename = argv[1]
        algorithm = argv[2]

        if filename[9] == "2":
            dimension = 12
        else:
            dimension = int(filename[8])

        game = Board(dimension, filename)

        if algorithm == "random":
            print("Now random:")
            game = Board(dimension, filename)
            start = time.time()
            iterations = random_only_legal_moves_algorithm(game)
            end = time.time()
            t = end - start
            write_random(t, iterations, dimension)
            load_statistics(algorithm)

            print(f"It took {end - start} seconds to run the random algorithm")

        elif algorithm == "breadth":
            print("Now breadth_first:")
            game = Board(dimension, filename)
            Breadth_first = BreadthFirst(game)
            start = time.time()
            Breadth_first.run()
            end = time.time()
            t = end - start
            write_breadth(t, iterations, dimension)

        elif algorithm == "randombreadth":
            game = Board(dimension, filename)
            Breadth_first_random_states = BreadthFirstRandomStates(game)
            start = time.time()
            Breadth_first_random_states.run()
            end = time.time()

            print(f"It took {end - start} seconds to run the BreadthFirstRandomStates algorithm")
            print()

        elif algorithm == "depth":

            df = DepthFirst(game)

            df.run2()

            bf = breadth_first(game)
            bf.run()
            breadth_first(game)

            df = DepthFirst(game)

            df.run()

    else:
        algorithm = argv[2]
        dimension = argv[3]
        data = load_statistics(algorithm, dimension)
        stat(algorithm, data)




    # nr = 10
    # results = []
    # heur_1 = []
    # for i in tqdm(range(nr)):
    #     game = Board(dimension, filename)
    #     legal_moves = random_only_legal_moves_algorithm(game)
    #     results.append(legal_moves)
    # print(f"{nr} iterations: the lowest number for legal moves is {min(results)} moves.")
    #
    # for i in tqdm(range(nr)):
    #     game = Board(dimension, filename)
    #     tiles_blocked_moves = tiles_blocked_heur(game)
    #     # print("Hello")
    #     heur_1.append(tiles_blocked_moves)
    # print(f"{nr} iterations: the lowest number for tiles_blocked_heur moves is {min(heur_1)} moves.")
