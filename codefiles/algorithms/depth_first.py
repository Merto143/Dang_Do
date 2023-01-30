import copy
import numpy as np

class DepthFirst:
    def __init__(self, game):
        self.board = game
        self.board.generate_moveability()
        self.node = -1


        self.states = [[copy.deepcopy(self.board.grid), "-"]]
        self.moves = []

        self.archive = [[copy.deepcopy(self.board.grid), "-"]]
        self.move_memory = []

        self.solution = []

        self.cars = self.board.get_moveable_cars()
        # self.stack_moves()

        self.visited = []
        self.stack = [[copy.deepcopy(self.board), "-"]]
        self.nodes = []
        self.nr_moves = 0
        # self.made_moves = []


    def find_solution(self):
        self.solution = []

        self.solution.insert(0, self.visited[-1][1])
        self.node = self.visited[-1][1][2]

        while self.node != 0:
            self.solution.insert(0, self.visited[self.node][1])
            new_node = self.visited[self.node][1][2]
            self.node = new_node

        return self.solution

    def run3(self):
        k = 1
        i = 1
        while self.stack:
            item = self.stack.pop()
            current_state = item[0]
            current_move = item[1]
            current_state.generate_moveability()
            print(f"Iteration {i}")
            self.node += 1

            # print(f"Current state: \n {current_state.grid} \n\n")

            if not (len(self.solution) != 0 and self.nr_moves >= len(self.solution)):
                # print(f"Current state has already been visited: {any(np.array_equal(current_state.grid, state) for state in self.visited)}")
                # print(f"{current_state.grid} has already been visited: {any(np.array_equal(current_state.grid, state) for state in self.visited)}\n")
                # self.history = list(zip(*self.visited))[0]
                # if not any(np.array_equal(current_state.grid, state) for state in self.history):
                self.visited.append([copy.deepcopy(current_state.grid), current_move])
                i += 1
                self.moves = self.create_moves(current_state)
                # print(moves)
                for move in self.moves:
                    # print(f"{move} is {any(np.array_equal(current_state.grid, state) for state in self.visited)}")
                    current_state.move_car(move[0], move[1])
                    current_state.set_car_coordinates()
                    # print(f"{current_state.grid} has already been visited: {any(np.array_equal(current_state.grid, state) for state in self.visited)}")
                    self.history = list(zip(*self.visited))[0]
                    if not any(np.array_equal(current_state.grid, state) for state in self.history):
                        self.stack.append([copy.deepcopy(current_state), move])
                        # self.nodes.append(self.node)
                        # self.made_moves.append(move)
                    # print(f"{self.stack[-1].grid} is the last added state")
                    current_state.undo_move(move[0], move[1])
                # print(f"Stack: {self.stack}")
                # print(f"Visited States:{self.visited}")
                # print("\n\n\n\n\n")
                # print(f"Length of stack: {len(self.stack)}")
                # print(f"Last added move: {self.made_moves[-1]}")
                # print(f"Node: {self.node}")
                # print(f"Total number of moves: {self.nr_moves}")
                # print(f"Possible moves viewed: {len(self.made_moves)}")
                print()

                if current_state.is_solved():
                    print(f"We have found solution nr {k}!")
                    k += 1
                    # print(f"We have visited {self.node} different states")
                    # print("The optimal solution is: ")
                    # print(self.nodes)
                    # print(self.moves[-1])
                    # print(self.visited[-1][0])
                    # print()
                    # print(self.visited[-1][1])
                    # print(len(self.visited))
                    # print(self.visited[753][0])
                    # print(self.visited[753][1])
                    # print("\n\n\n")
                    # print(self.visited[754][0])
                    # print(self.visited[754][1])
                    # print(self.visited[752][0])
                    # print(self.visited[752][1])
                    for move in self.find_solution():
                        print(move)
                    print(f"Total moves of: {len(self.solution)}")
                    # break
                    # self.nr_moves = len(self.find_solution())

        print("We have visited all possible states with depth first")

    def get_next_move(self):
        if self.states:
            return self.states.pop()

    # def get_next_move(self):
    #     if self.moves:
    #         return self.moves.pop()


    # def build_children(self, game):
    #     options = game.get_all_moves()
    #     print(f"{len(options)}")
    #
    #     for option in options:
    #         new_state = copy.deepcopy(game)
    #         new_state.move_car(option[0], option[1])
    #         # if new_state not in self.states:
    #         if not any(np.array_equal(new_state.grid, state.grid) for state in self.states):
    #             self.states.append(new_state)
    #             print(f"{option}")
    #             print(f"{new_state.grid}")
    #
    # def check_solution(self, game):
    #     sol = []
    #     print("We have a solution")
    #     return sol


    # def run(self):
    #     i = 1
    #     print(f"{self.states[0][0]}")
    #
    #     while self.states:
    #         new_state = self.get_next_move()
    #         print(new_state)
    #         print(f"Before moving car: {self.board.grid}")
    #         self.board.set_car_coordinates()
    #         self.board.move_car(new_state[0], new_state[1])
    #         print(f"After moving car: {self.board.grid}")
    #
    #         self.history = list(zip(*self.archive))[0]
    #
    #         if not any(np.array_equal(self.board.grid, state) for state in self.history):
    #             print(f"State number {i}")
    #             print(f"{self.board.grid} is a new state")
    #             i += 1
    #
    #         if self.board.is_solved():
    #             pass
    #         else:
    #             pass

        #     if not self.board.is_solved():
        #         self.build_children(new_state)
        #         print("\n\n")
        #     else:
        #         self.check_solution(new_state)
        #         print("Game is solved")
        #
        #
        # print(f"{self.states[0].grid}")


    # def run2(self):
    #
    #     print(f"the begin grid looks like: {self.board.grid}")
    #     i = 1
    #     k = 1
    #     # while self.states:
    #     for j in range(10):
    #         new_move = self.get_next_move()
    #         print(f"Next in stack: {new_move[-1]}")
    #         print(f"Grid memory: {self.archive[-1][0]}")
    #         self.board.grid = copy.deepcopy(self.archive[new_move[-1]][0])
    #         self.board.set_car_coordinates()
    #
    #         self.board.move_car(new_move[0], new_move[1])
    #         print(f"{self.archive}, is this list empty?")
    #         self.history = list(zip(*self.archive))[0]
    #
    #         if not any(np.array_equal(self.board.grid, state) for state in self.history):
    #             print(f"State number {k}")
    #             k += 1
    #             print(f"state has not been seen yet")
    #             self.moves.append(new_move)
    #             self.states.append([copy.deepcopy(self.board.grid), new_move])
    #             self.archive.append(new_state[0])
    #             self.node += 1
    #
    #             self.board.generate_moveability()
    #             self.stack_moves()
    #         else:
    #             print("\n\n\n")
    #             print(f"Move: {new_move}, state has already been seen, don't save")
    #             print("\n\n\n")
    #
    #         if self.board.is_solved():
    #             print(f"Solution {i}")
    #             i += 1
    #             break
    #         else:
    #             print(f"Current node: {self.board.grid}")
    #             print("\n\n")
    #             print(f"All moves in the list: {self.moves}")
    #             print("\n\n")
    #             print(f"All states/grids in the list: {self.states}")
    #             print("\n\n")


            # if not self.board.is_solved():
            #     self.build_children(new_state)
            #     print("\n\n")
            # else:
            #     self.check_solution(new_state)
            #     print(f"Game is solved with in total {len(self.check_solution())} steps")

    def create_moves(self, game):
        moves = []
        for car in game.get_moveable_cars():
            for direction in car.get_legal_moves():
                new_move = [car, direction, self.node]
                moves.append(new_move)
        return moves

    def stack_moves(self):
            for car in self.board.get_moveable_cars():
                for direction in car.get_legal_moves():
                    self.node += 1
                    new_move = [car, direction, self.node]
                    self.states.append(new_move)
