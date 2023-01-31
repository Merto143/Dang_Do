import copy
import numpy as np

class DepthFirst:

    def __init__(self, game):
        self.board = game
        self.board.generate_moveability()
        self.node = -1

        self.solution = []

        # self.cars = self.board.get_moveable_cars()

        self.depth = 0
        self.visited = []
        self.nr_moves = 0
        self.stack = [[copy.deepcopy(self.board), "-", self.depth]]
        self.nodes = []
        self.best_solution = 0


    def go_to_next_state(self):
        return self.stack.pop()


    def increase_node(self):
        self.node += 1


    def get_state(self, state):
        current_state = state[0]
        return current_state


    def get_move(self, state):
        current_move = state[1]
        return current_move

    # def set_depth(self):
    #
    #     return self.depth


    def add_to_visited(self, state, move, depth):
        self.visited.append([copy.deepcopy(state.grid), move, depth])


    def create_moves(self, game):
        moves = []
        for car in game.get_moveable_cars():
            for direction in car.get_legal_moves():
                new_move = [car, direction, self.node]
                print(f"New move: {new_move}")
                moves.append(new_move)
        print(f"moves: {moves}")
        return moves


    def add_to_stack(self, state, move, depth):
        self.stack.append([copy.deepcopy(state), move, depth])


    def run(self):
        k = 1
        i = 1
        while self.stack:
            item = self.go_to_next_state()
            print(f"Iteration {i}")
            current_state = self.get_state(item)
            current_state.generate_moveability()
            current_state.set_car_coordinates()
            current_move = self.get_move(item)
            self.increase_node()

            depth = self.depth

            # depth = self.set_depth()


            print(len(self.stack))
            print(current_state.grid)
            print(current_move)

            if not (len(self.solution) != 0 and self.nr_moves >= len(self.solution)):
                self.add_to_visited(current_state, current_move, depth)
                i += 1

                if not current_state.is_solved():
                    self.moves = self.create_moves(current_state)
                    # print(len(self.moves))
                    for move in self.moves:
                        current_state.move_car(move[0], move[1])
                        current_state.set_car_coordinates()
                        self.history = list(zip(*self.visited))[0]
                        if not any(np.array_equal(current_state.grid, state) for state in self.history):
                            self.add_to_stack(current_state, move, depth)
                            # print(move)
                        current_state.undo_move(move[0], move[1])
                    print()

            # print(current_state.grid)
            # print()
            # print(self.visited)

            if current_state.is_solved():
                print(f"We have found solution nr {k}!")
                k += 1
                self.display_solution()
                print(f"Total moves of: {len(self.solution)}")
                if len(self.solution) <= self.best_solution or self.best_solution == 0:
                    self.best_solution = len(self.solution)
                print(f"Our best solution so far: {self.best_solution}")
                print("\n\n")

        print("We have visited all possible states with depth first")
        print(f"best solution is: {self.best_solution}")


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
        for move in self.find_solution():
            print(move)
