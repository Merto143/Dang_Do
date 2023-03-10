from sys import argv
from codefiles.classes.car import Car
from codefiles.classes.board import Board
from codefiles.visualisations.visuals import grid_visual, write_random, write_breadth, write_randombreadth, write_depth, write_beam, load_statistics, histograms, scatterplot
from codefiles.algorithms.algorithms import random_only_legal_moves_algorithm
from codefiles.algorithms.depth_first import DepthFirst
from codefiles.algorithms.depth_first_all import DF_all
from codefiles.algorithms.breadth_first import BreadthFirst
from codefiles.algorithms.breadth_first_random_states import BreadthFirstRandomStates
from codefiles.algorithms.beam_search import BeamSearch


from tqdm import tqdm
import time


if __name__ == "__main__":

    if len(argv) != 4 and argv[2] != "depth_all":
        print("Usage: python3 main.py [filename] [algorithm] [nr of runs] OR python3 main.py statistics [algorithm] [dimension]")
        exit(1)

    if argv[1] == "statistics":
        algorithm = argv[2]
        dimension = argv[3]
        data = load_statistics(algorithm, dimension)
        histograms(algorithm, data, dimension)
        scatterplot(algorithm, data, dimension)

    else:

        filename = argv[1]
        algorithm = argv[2]
        if algorithm == "depth_all" and len(argv) == 5:
            cut = int(argv[3])
            max_runs = int(argv[4])
        else:
            cut = 0
            max_runs = int(argv[3])
        n_runs = 0

        if filename[9] == "2":
            dimension = 12
        else:
            dimension = int(filename[8])

        game = Board(dimension, filename)
        grid_visual(game)


        if algorithm == "random":
            while n_runs < max_runs:
                print("Now random:")
                game = Board(dimension, filename)
                start = time.time()
                visited_states = random_only_legal_moves_algorithm(game)
                end = time.time()
                runtime = end - start
                # write_random(runtime, visited_states, dimension)
                n_runs += 1

                print(f"It took {runtime} seconds to run the random algorithm.")

            # grid_visual(game)

        elif algorithm == "breadth":
            game = Board(dimension, filename)
            breadth = BreadthFirst(game)
            start = time.time()
            breadth.run()
            end = time.time()
            runtime = end - start
            # write_breadth(runtime, len(breadth.get_visited_states()), dimension, int(len(breadth.get_solution()) / 2))

            print(f"It took {runtime} seconds to run the Breadth First Search algorithm.")

            # grid_visual(game)

        elif algorithm == "randombreadth":
            start_run = time.time()
            random_repeats = 1
            while n_runs < max_runs:
                game = Board(dimension, filename)

                start = time.time()
                randombreadth = BreadthFirstRandomStates(game, random_repeats)
                randombreadth.run()
                end = time.time()

                runtime = end - start
                write_randombreadth(runtime, len(randombreadth.get_visited_states()), dimension, int(len(randombreadth.get_solution()) / 2))
                n_runs += 1

                print(f"It took {runtime} seconds to run the optimized random algorithm.")

            # grid_visual(game)

        elif algorithm == "depth":
            start_run = time.time()
            while n_runs < max_runs:
                game = Board(dimension, filename)
                depth = DepthFirst(game)

                start = time.time()
                depth.run()
                end = time.time()

                runtime = end - start
                write_depth(runtime, len(depth.get_visited_states()) - 1, dimension, len(depth.get_solution()))
                n_runs += 1

                print(f"It took {runtime} seconds to run the DepthFirst Search algorithm.")

            # grid_visual(game)

        elif algorithm == "depth_all":
            start_run = time.time()
            while n_runs < max_runs:
                game = Board(dimension, filename)

                df = DF_all(game, cut)

                start = time.time()
                df.run()
                end = time.time()

                runtime = end - start
                write_depth(runtime, len(df.get_visited_states()) - 1, dimension, len(df.get_solution()))
                n_runs += 1

                print(f"It took {runtime} seconds to run the DF_all Search algorithm.")

        elif algorithm == "beam":

                beam = BeamSearch(game)

                start = time.time()
                beam.run()
                end = time.time()

                runtime = end - start
                # write_beam(time, beam.get_visited_states(), dimension, int(len(beam.get_solution()) / 2) )

                print(f"It took {runtime} seconds to run the Beam Search algorithm.")

            # grid_visual(game)
