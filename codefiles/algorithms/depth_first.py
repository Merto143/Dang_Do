import copy
import numpy as np

class DepthFirst:
    """ Depth First Search until first solution is found. """

    def __init__(self, game):
        self.board = game
        self.board.generate_moveability()
        self.node = 0

        self.depth = 0
        self.visited = [[copy.deepcopy(self.board.grid), "-", self.depth]]
        self.moves = []
        self.stack = []
        self.best_solution = None

        self.clear_solutions()
        self.create_next_moves()


    def run(self):
        """ Runs DepthFirst algorithm on given game. """

        while self.stack:
            item = self.pop_next_item()
            self.board.grid = copy.deepcopy(self.visited[item[2]][0])
            self.board.set_car_coordinates()
            self.board.move_car(item[0], item[1])

            if not self.grid_seen_before():
                self.depth = self.get_depth(item)
                self.moves.append(item)
                self.visited.append([self.board.grid, item])
                self.increase_node()

                self.board.generate_moveability()
                self.create_next_moves()

            if self.board.is_solved():
                self.display_solution()
                self.compare_solutions()
                break

        if self.any_solution_yet():
            print(f"Our best solution is {self.best_solution} number of moves.")
        else:
            print(f"We have found no solution.")


    def pop_next_item(self):
        """ Pops next item on top of self.stack. """

        return self.stack.pop()


    def grid_seen_before(self):
        """ Returns whether current state/grid has been seen before. """

        return (any(np.array_equal(self.board.grid, state[0]) for state in self.visited))


    def increase_node(self):
        """ Increases self.node by 1 unit. """

        self.node += 1


    def get_depth(self, state):
        """ Returns the depth/generation of state. """

        self.depth = state[3]
        return self.depth


    def create_next_moves(self):
        """ Creates all possible moves for self.board.
            Stacks these moves onto self.stack. """

        for car in self.board.get_moveable_cars():
            for direction in car.get_legal_moves():
                move = [car, direction, self.node, self.depth + 1]
                self.stack.append(move)


    def find_solution(self):
        """ Traces back the solution from solved state to start state via nodes.
            Then returns solution as list of moves. """

        self.clear_solutions()

        self.find_final_node()

        while self.not_at_root_node():
            self.solution.insert(0, self.visited[self.current_node][1])
            self.set_new_node()

        return self.solution


    def not_at_root_node(self):
        """ Returns whether we are back to the root node. """

        return (self.current_node != 0)


    def clear_solutions(self):
        """ Sets self.solution to empty list. """

        self.solution = []


    def set_new_node(self):
        """ Finds next node in solution sequence. """

        self.new_node = self.visited[self.current_node][1][2]
        self.current_node = self.new_node


    def find_final_node(self):
        """ Returns the node of solved state in order to trace back to previous state. """

        self.solution.insert(0, self.visited[-1][1])
        self.current_node = self.visited[-1][1][2]


    def display_solution(self):
        """ Displays the message that we have found a solution. """

        print(f"We have found a solution:\n")
        self.print_moves_sequence()
        print(f"Solution is {len(self.find_solution())} moves long")


    def print_moves_sequence(self):
        """ Prints the sequence of moves that is the solution. """

        for move in self.find_solution():
            print(f"[{move[0]}, {move[1]}]")


    def compare_solutions(self):
        """ Compares newly found solution to current best solution.
            If better, declares it as new best solution. """

        if not self.any_solution_yet() or self.better_than_best_solution():
            if self.any_solution_yet() and better_than_best_solution():
                print(f"Found a better solution: {self.get_length_solution()} < {self.best_solution}")
            self.set_new_best_solution()


    def any_solution_yet(self):
        """ Checks if there is any solution is found already. """

        return (self.best_solution is not None)


    def better_than_best_solution(self):
        """ Compares solution to current best solution. """

        return (self.get_length_solution() < self.best_solution)


    def set_new_best_solution(self):
        """ Sets newly found solution to best solution so far. """

        self.best_solution = self.get_length_solution()


    def get_visited_states(self):
        """ Returns all states that we have visited thus far. """

        return self.visited


    def get_solution(self):
        """ Returns the found solution. """

        return self.solution


    def get_length_solution(self):
        """ Returns the length of the found solution. """

        return (len(self.find_solution()))
