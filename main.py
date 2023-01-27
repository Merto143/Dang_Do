from sys import argv
from codefiles.classes.car import Car
from codefiles.classes.board import Board
from codefiles.visualisations.visuals import *
from codefiles.algorithms.algorithms import random_only_legal_moves_algorithm, random_all_moves_algorithm
from codefiles.algorithms.algorithms import breadth_first
from codefiles.algorithms.depth_first import DepthFirst
from codefiles.algorithms.breadth_first import BreadthFirst
from codefiles.algorithms.breadth_first_random_states import BreadthFirstRandomStates

from tqdm import tqdm
import time



if __name__ == "__main__":
    if len(argv) > 2:
        print("Usage: python3 main.py [filename] OR python3 visualisations/visuals.py")
        exit(1)
    elif len(argv) == 1:
        load_statistics()
        stat()
    elif len(argv) == 2:
        filename = argv[1]

        if filename[9] == "2":
            dimension = 12
        else:
            dimension = int(filename[8])
    game = Board(dimension, filename)
# <<<<<<< HEAD
#     df = DepthFirst(game)
#
#     df.run()
# =======
#     grid_visual(game)
#     # breadth_first(game)
#
# >>>>>>> 9a71f9c505a2c9e0b5b735b33d08007da6afb0bc
    print("BreadthFirst:")
    start = time.time()
    Breadth_first = BreadthFirst(game)
    Breadth_first.run()
    end = time.time()

    print(f"It took {end - start} seconds to run the BreadthFirst algorithm")
    print()


    game = Board(dimension, filename)

    print("BreadthFirstRandomStates:")
    start = time.time()
    Breadth_first_random_states = BreadthFirstRandomStates(game)
    Breadth_first_random_states.run()
    end = time.time()

    print(f"It took {end - start} seconds to run the BreadthFirstRandomStates algorithm")
    print()
    

    print("Now random:")
    game = Board(dimension, filename)
    start = time.time()
    random_only_legal_moves_algorithm(game)
    end = time.time()

    print(f"It took {end - start} seconds to run the random algorithm")

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


# dit is wat we hiervoor gebruikten om het een enkele keer te laten runnen
    # game = Board(dimension, filename)
    # game.visual()
    # all_moves = random_all_moves_algorithm(game)
    # game = Board(dimension, filename)
    # legal_moves = random_only_legal_moves_algorithm(game)
    #
    # print(f"All moves: {all_moves} try's to solve the problem")
    # print(f"Legal moves: {legal_moves} try's to solve the problem")
