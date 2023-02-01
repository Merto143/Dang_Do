import copy
import numpy as np

from codefiles.algorithms.depth_first import DepthFirst

class DF_all(DepthFirst):
    """ Depth first search until all possible solutions are found.
        Algorithm does not search deeper in tree than best current solution.
        Algorithm skips states that already have been seen and have equal or higher depth to previously seen equal state.
        Takes a lot of time to run, but should find the best solution. """

    def __init__(self, game):
        self.board = game
        self.board.generate_moveability()
        self.node = 0

        self.k = 1

        self.solution = []

        self.depth = 0
        self.visited = [[copy.deepcopy(self.board.grid), "-", self.depth]]
        self.moves = []
        self.stack = []
        self.nodes = []
        self.best_solution = None
        self.list = []

        self.create_next_moves()

    def run(self):
        # i = 1
        while self.stack:
            # print(f"Iteration {i}")
            # i += 1
            item = self.pop_next_item()
            # print(item)
            self.board.grid = copy.deepcopy(self.visited[item[2]][0])
            self.board.set_car_coordinates()
            self.board.move_car(item[0], item[1])
            self.depth = self.get_depth(item)

            self.seen_grids = list(zip(*self.visited))[0]
            if self.best_solution is None or self.depth < self.best_solution:
            # if not any(np.array_equal(self.board.grid, grid) for grid in self.seen_grids):
                proceed = True
                for state in self.visited:
                    if (np.array_equal(self.board.grid, state[0]) and self.depth != 0) and self.depth + 1 >= state[2]:
                        # print(f"Already seen: {np.array_equal(self.board.grid, state[0])}")
                        # print(f"Too deep as well: {self.depth + 1 > state[2]}")
                        proceed = False
                        break
                # if not any(np.array_equal(self.board.grid, state[0]) and self.depth + 1 > state[2] for state in self.visited):
                if proceed:
                    # print("entered!")
                    # print(f"")
                    # print(f"")
                    # print(f"{not any(np.array_equal(self.board.grid, state[0]) for state in self.visited) or not any(self.depth + 1 > state[2] for state in self.visited)}")
                    self.moves.append(item)
                    self.visited.append([self.board.grid, item, self.depth + 1])
                    self.increase_node()

                    self.board.generate_moveability()
                    self.create_next_moves()



                if self.board.is_solved():
                    self.display_solution()
                    # if self.best_solution is None or self.get_length_solution() < self.best_solution:
                    #     if self.best_solution is not None and self.get_length_solution() < self.best_solution:
                    #         print(f"Found a better solution: {self.get_length_solution()} < {self.best_solution}")
                    #     self.best_solution = self.get_length_solution()
                    self.compare_solutions()

        print(f"Our best solution is {self.best_solution}")


    def display_solution(self):
        print(f"We have found solution nr {self.k}:")
        self.k += 1
        for move in self.find_solution():
            print(move)
        print(f"Solution is {len(self.find_solution())} moves long")
