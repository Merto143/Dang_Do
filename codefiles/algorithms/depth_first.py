import copy
import numpy as np

class DepthFirst:

    def __init__(self, game):
        self.board = game
        self.board.generate_moveability()
        self.node = 0

        self.solution = []

        self.start_depth = 0
        self.visited = [[copy.deepcopy(self.board.grid), "-"]]
        self.moves = []
        self.stack = []
        self.nodes = []
        self.best_solution = 0
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
        current_depth = state[2]
        return current_depth


    def add_to_visited(self):
        self.visited.append([self.board, self.move, self.current_depth])


    def create_next_moves(self):
        for car in self.board.get_moveable_cars():
            for direction in car.get_legal_moves():
                move = [car, direction, self.node]
                self.stack.append(move)


    def add_to_stack(self, state, move, depth):
        self.stack.append([copy.deepcopy(state), move, depth])


    def run(self):
        while self.stack:
            item = self.pop_next_item()
            # print(f"Iteration {self.node + 2}")
            self.board.grid = copy.deepcopy(self.visited[item[2]][0])
            self.board.set_car_coordinates()
            self.board.move_car(item[0], item[1])

            self.seen_grids = list(zip(*self.visited))[0]
            if not any(np.array_equal(self.board.grid, grid) for grid in self.seen_grids):
                self.moves.append(item)
                self.visited.append([self.board.grid, item])
                self.node += 1

                self.board.generate_moveability()
                self.create_next_moves()

            if self.board.is_solved():
                self.display_solution()
                break


        #     self.current_state.generate_moveability()
        #     self.current_state.set_car_coordinates()
        #     self.current_move = self.get_move(item)
        #     print(self.current_move)
        #     self.current_depth = self.get_depth(item)
        #     self.increase_node()
        #     self.add_to_visited()
        #
        #     if self.best_solution == 0 or current_depth < self.best_solution:
        #
        #         if not self.current_state.is_solved():
        #             self.moves = self.create_moves(self.current_state)
        #             for move in self.moves:
        #                 current_state.move_car(move[0], move[1])
        #                 current_state.set_car_coordinates()
        #                 if not any(np.array_equal(current_state.grid, state[0].grid) for state in self.visited):
        #                     self.add_to_stack(self.current_state, move, current_depth + 1)
        #                 current_state.undo_move(move[0], move[1])
        #             # print()
        #         else:
        #             # print(f"We have found solution nr {k}!")
        #             k += 1
        #             self.display_solution()
        #             # print(f"Total moves of: {len(self.solution)}")
        #             new_sol = len(self.solution)
        #             if new_sol <= self.best_solution or self.best_solution == 0:
        #                 self.best_solution = new_sol
        #             # print(f"Our best solution so far: {self.best_solution}")
        #             # print("\n\n")
        #             break
        #
        # print(f"We have visited in total {len(self.visited)} states with depth first")
        # print(f"best solution is: {self.best_solution}")


    def find_solution(self):
        self.solution = []

        self.solution.insert(0, self.visited[-1][1])
        current_node = self.visited[-1][1][2]
        # print(current_node)
        # print(len(self.visited))

        while current_node != 0:
            self.solution.insert(0, self.visited[current_node][1])
            new_node = self.visited[current_node][1][2]
            current_node = new_node

        return self.solution


    def display_solution(self):
        print(f"We have found a solution:")
        for move in self.find_solution():
            print(move)
        print(f"Solution is {len(self.find_solution())//2} moves long")
