import copy
import numpy as np

from codefiles.algorithms.depth_first import DepthFirst

class DF_all(DepthFirst):
    """ Depth first search until all possible solutions are found.
        Algorithm does not search deeper in tree than best current solution.
        It is possible to give this algorithm an extra parameter, namely the cut.
        This is the distance in steps (up the tree), for which we don't want to
        consider a state in case we have seen an identical state deeper in the tree. """

    def __init__(self, game, cut):
        """ Initializer. """
        self.board = game
        self.board.generate_moveability()
        self.node = 0
        self.nr_sol = 0
        self.cut = int(cut)

        self.depth = 0
        self.visited = [[copy.deepcopy(self.board.grid), "-", self.depth]]
        self.moves = []
        self.stack = []
        self.best_solution = None

        self.clear_solutions()
        self.create_next_moves()


    def run(self):
        """ Runs DF_all algorithm on given game. """

        while self.stack:
            item = self.pop_next_item()
            self.board.grid = copy.deepcopy(self.visited[item[2]][0])
            self.board.set_car_coordinates()
            self.board.move_car(item[0], item[1])
            self.depth = self.get_depth(item)

            if not self.any_solution_yet() or self.not_too_deep():
                self.proceed = True
                self.compare_to_visited()
                if self.proceed:
                    self.moves.append(item)
                    self.visited.append([self.board.grid, item, self.depth + 1])
                    self.increase_node()

                    self.board.generate_moveability()
                    self.create_next_moves()

                if self.board.is_solved():
                    self.display_solution()
                    if not self.any_solution_yet() or self.better_than_best_solution():
                        if self.any_solution_yet() and self.better_than_best_solution():
                            print(f"Found a better solution: {self.get_length_solution()} < {self.best_solution}")
                        self.set_new_best_solution()
                    self.compare_solutions()

        print(f"Our best solution is {self.best_solution} number of moves.")


    def not_too_deep(self):
        """ Returns wheter we are too far into the tree in terms of depth. """

        return (self.depth < self.best_solution)


    def compare_to_visited(self):
        """ Compares current grid to grids in self.visited.
            Sets self.proceed to False if this state can not lead to a new best solution. """

        for state in self.visited:
            if (np.array_equal(self.board.grid, state[0]) and self.depth != 0) and self.depth + 1 >= state[2] - self.cut:
                self.proceed = False
                break


    def display_solution(self):
        """ Displays the message that we have found a solution. """

        self.nr_sol += 1
        print(f"We have found solution {self.nr_sol}:")
        self.print_moves_sequence()
        print(f"Solution {self.nr_sol} is {len(self.find_solution())} moves long.")
