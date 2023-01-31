from sys import argv
from codefiles.classes.car import Car
from codefiles.classes.board import Board
from codefiles.visualisations.visuals import *
from codefiles.algorithms.algorithms import random_only_legal_moves_algorithm, random_all_moves_algorithm
from codefiles.algorithms.algorithms import breadth_first
from codefiles.algorithms.depth_first import DepthFirst
from codefiles.algorithms.depth_first_break import DepthFirst_break
from codefiles.algorithms.depth_first_depth import DepthFirst_depth


from codefiles.algorithms.algorithms import breadth_first
from codefiles.algorithms.algorithms import breadth_first
from codefiles.algorithms.breadth_first import BreadthFirst
from codefiles.algorithms.breadth_first_random_states import BreadthFirstRandomStates


from tqdm import tqdm
import time
import subprocess


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: python3 main.py [filename] [algorithm] [nr of runs] OR python3 main.py statistics [algorithm] [dimension]")
        exit(1)

    elif argv[1] == "statistics":
        algorithm = argv[2]
        dimension = argv[3]
        data = load_statistics(algorithm, dimension)
        histograms(algorithm, data, dimension)

    else:
        filename = argv[1]
        algorithm = argv[2]
        max_runs = int(argv[3])

        if filename[9] == "2":
            dimension = 12
        else:
            dimension = int(filename[8])

        game = Board(dimension, filename)

        if algorithm == "random":
            n_runs = 0
            start_run = time.time()

            while n_runs < max_runs:
                print("Now random:")
                game = Board(dimension, filename)
                start = time.time()
                visited_states = random_only_legal_moves_algorithm(game)
                end = time.time()
                time = end - start
                write_random(time, visited_states, dimension)
                n_runs += 1

                print(f"It took {time} seconds to run the random algorithm")

        elif algorithm == "breadth":
            print("Now breadth_first:")
            game = Board(dimension, filename)
            Breadth_first = BreadthFirst(game)
            start = time.time()
            Breadth_first.run()
            end = time.time()
            time = end - start
            write_breadth(time, len(Breadth_first.get_visited_states()), dimension, len(Breadth_first.get_solution()))

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

            df.run()


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
