from sys import argv
from codefiles.classes.car import Car
from codefiles.classes.board import Board
# from codefiles.visualisations.visuals import *
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

        elif algorithm == "depth":
            df = DepthFirst(game)

            df.run()

        elif algorithm == "depth_break":

            df = DepthFirst_break(game)

            df.run()

        elif algorithm == "depth_depth":

            df = DepthFirst_depth(game)

            df.run()

        else:

            algorithm = argv[2]
            dimension = argv[3]
            data = load_statistics(algorithm, dimension)
            stat(algorithm, data)
