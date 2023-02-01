from sys import argv
from codefiles.classes.car import Car
from codefiles.classes.board import Board
from codefiles.visualisations.visuals import grid_visual, write_random, write_breadth, write_randombreadth, write_depth, write_beam, load_statistics, histograms
from codefiles.algorithms.algorithms import random_only_legal_moves_algorithm
from codefiles.algorithms.depth_first import DepthFirst
from codefiles.algorithms.depth_first_break import DepthFirst_break
from codefiles.algorithms.depth_first_depth import DepthFirst_depth
from codefiles.algorithms.breadth_first import BreadthFirst
from codefiles.algorithms.breadth_first_random_states import BreadthFirstRandomStates
from codefiles.algorithms.beam_search import BeamSearch


from tqdm import tqdm
import time


if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: python3 main.py [filename] [algorithm] [nr of runs] OR python3 main.py statistics [algorithm] [dimension]")
        exit(1)

    elif argv[1] == "statistics":
        algorithm = argv[2]
        dimension = argv[3]
        data = load_statistics(algorithm, dimension)
        histograms(algorithm, data, dimension)
        # scatterplot(algorithm, data, dimension)

    else:

        filename = argv[1]
        algorithm = argv[2]
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

                print(f"It took {runtime} seconds to run the random algorithm")

            grid_visual(game)

        elif algorithm == "breadth":
            game = Board(dimension, filename)
            breadth = BreadthFirst(game)
            start = time.time()
            breadth.run()
            end = time.time()
            runtime = end - start
            # write_breadth(runtime, len(breadth.get_visited_states()), dimension, int(len(breadth.get_solution()) / 2))

            print(f"It took {runtime} seconds to run the Breadth First Search algorithm")

            grid_visual(game)

        elif algorithm == "randombreadth":
            start_run = time.time()
            while n_runs < max_runs:
                game = Board(dimension, filename)
                randombreadth = BreadthFirstRandomStates(game)

                start = time.time()
                randombreadth.run()
                end = time.time()

                runtime = end - start
                # write_randombreadth(runtime, len(randombreadth.get_visited_states()), dimension, int(len(randombreadth.get_solution()) / 2))
                n_runs += 1

                print(f"It took {runtime} seconds to run the optimized random algorithm")

            grid_visual(game)

        elif algorithm == "depth":
            start_run = time.time()
            while n_runs < max_runs:
                game = Board(dimension, filename)
                depth = DepthFirst(game)

                start = time.time()
                depth.run()
                end = time.time()

                runtime = end - start
                # write_depth(runtime, depth.get_visited_states(), dimension, depth.get_solution())
                n_runs += 1

                print(f"It took {runtime} seconds to run the Depth First Search algorithm")

            grid_visual(game)

        elif algorithm == "beam":
            start_run = time.time()
            while n_runs < runs_max:
                game = Board(dimension, filename)
                beam = BeamSearch(game)

                start = time.time()
                beam.run()
                end = time.time()

                runtime = end - start
                # write_beam(time, beam.get_visited_states(), dimension, int(len(beam.get_solution()) / 2) )

                print(f"It took {runtime} seconds to run the Depth First Search algorithm")

            grid_visual(game)

        elif algorithm == "depth_break":

            df = DepthFirst_break(game)

            df.run()

        elif algorithm == "depth_depth":

            df = DepthFirst_depth(game)

            df.run()

        elif algorithm == "df2":

            df2 = DF2(game)

            df2.run()

        elif algorithm == "df":

            df = DF(game)

            df.run()


        # if algorithm == "BeamSearch":
        #     game = Board(dimension, filename)
        #     start = time.time()
        #     bs = BeamSearch(game, 3)
        #     bs.run()
        #     end = time.time()
        #     t = end - start
        #     # write_random(t, iterations, dimension)
        #
        #     print(f"It took {end - start} seconds to run the random algorithm")
        #
        # elif algorithm == "random_memory":
        #     game = Board(dimension, filename)
        #     start = time.time()
        #     iterations = random_only_legal_moves_algorithm_with_memory(game)
        #     end = time.time()
        #     t = end - start
        #     # write_random(t, iterations, dimension)
        #
        #     print(f"It took {end - start} seconds to run the random algorithm")
        #
        # elif algorithm == "random":
        #     game = Board(dimension, filename)
        #     start = time.time()
        #     iterations = random_only_legal_moves_algorithm(game)
        #     end = time.time()
        #     t = end - start
        #     # write_random(t, iterations, dimension)
        #
        #     print(f"It took {end - start} seconds to run the random algorithm")
        #
        # elif algorithm == "random_id":
        #     game = Board(dimension, filename)
        #     start = time.time()
        #     iterations = random_only_legal_moves_algorithm_id(game)
        #     end = time.time()
        #     t = end - start
        #     # write_random(t, iterations, dimension)
        #
        #     print(f"It took {end - start} seconds to run the random algorithm")
