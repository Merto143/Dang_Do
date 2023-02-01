import copy
import numpy as np

class DepthFirst:
    """ Depth first search until first solution is found. """

    def __init__(self, game):
        self.start = game
        self.board = game
        self.board.generate_moveability()
        self.node = 0

        self.solution = []

        # self.start_depth = 0
        self.depth = 0
        self.visited = [[copy.deepcopy(self.board.grid), "-", self.depth]]
        self.moves = []
        self.stack = []
        self.nodes = []
        self.best_solution = None
        self.list = []

        self.create_next_moves()


    def pop_next_item(self):
        return self.stack.pop()


    def increase_node(self):
        self.node += 1


    def get_state(self, state):
        current_state = state[0]
        return current_state


    def get_move(self, state):
        current_move = state[1]
        return current_move


    def get_depth(self, state):
        depth = state[3]
        return depth


    def add_to_visited(self):
        self.visited.append([self.board, self.move, self.current_depth])


    def create_next_moves(self):
        for car in self.board.get_moveable_cars():
            for direction in car.get_legal_moves():
                move = [car, direction, self.node, self.depth + 1]
                self.stack.append(move)


    def add_to_stack(self, state, move, depth):
        self.stack.append([copy.deepcopy(state), move, depth])


    def run(self):
        while self.stack:
            item = self.pop_next_item()
            self.board.grid = copy.deepcopy(self.visited[item[2]][0])
            self.board.set_car_coordinates()
            self.board.move_car(item[0], item[1])

            self.seen_grids = list(zip(*self.visited))[0]
            if not any(np.array_equal(self.board.grid, grid) for grid in self.seen_grids):
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

        if self.best_solution is not None:
            print(f"Our best solution is {self.best_solution}")
        else:
            print(f"We have found no solution.")




    def find_solution(self):
        self.solution = []

        self.solution.insert(0, self.visited[-1][1])
        current_node = self.visited[-1][1][2]

        while current_node != 0:
            self.solution.insert(0, self.visited[current_node][1])
            new_node = self.visited[current_node][1][2]
            current_node = new_node

        return self.solution

    def display_solution(self):
        print(f"We have found a solution:")
        for move in self.find_solution():
            print(move)
        print(f"Solution is {len(self.find_solution())} moves long")


    def get_visited_states(self):
        return self.visited


    def get_solution(self):
        return self.solution


    def get_length_solution(self):
        return (len(self.find_solution()))


    def compare_solutions(self):
        if self.best_solution is None or self.get_length_solution() < self.best_solution:
            if self.best_solution is not None and self.get_length_solution() < self.best_solution:
                print(f"Found a better solution: {self.get_length_solution()} < {self.best_solution}")
            self.best_solution = self.get_length_solution()
