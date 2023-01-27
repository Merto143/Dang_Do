import copy
import numpy as np

class DepthFirst:
    def __init__(self, game):
        self.board = game
        self.board.generate_moveability()
        self.node = 0


        self.states = [[copy.deepcopy(self.board.grid), "-"]]
        self.moves = []

        self.grid_memory = []
        self.move_memory = []

        self.solution = []

        self.cars = self.board.get_moveable_cars()
        self.stack_moves()


    def get_next_state(self):
        return self.states.pop()

    def get_next_move(self):
        return self.moves.pop()


    # def any_moves_pruned(self, game):
    #     options = game.get_all_moves()
    #
    #     for option in options:
    #         new_state = copy.deepcopy(game)
    #         new_state.move_car(option[0], option[1])
    #         # if new_state not in self.states:
    #         if not any(np.array_equal(new_state.grid, state.grid) for state in self.states):
    #             print(f"{option}")
    #             print(f"{new_state.grid}")
    #             return option
    #     return None


    def build_children(self, game):
        options = game.get_all_moves()
        print(f"{len(options)}")

        for option in options:
            new_state = copy.deepcopy(game)
            new_state.move_car(option[0], option[1])
            # if new_state not in self.states:
            if not any(np.array_equal(new_state.grid, state.grid) for state in self.states):
                self.states.append(new_state)
                print(f"{option}")
                print(f"{new_state.grid}")


        # if not any(np.array_equal(new_state.grid, state.grid) for state in self.states):
        #     game.generate_moveability()
        #
        #     for car in game.get_moveable_cars():
        #         for direction in car.get_legal_moves():
        #             new_move = [car, direction]
        #
        #             if not
        #             self.moves.append(new_move)

    def check_solution(self, game):
        sol = []
        print("We have a solution")
        return sol


    def run(self):
        print(f"{self.states[0][0]}")

        while self.states:
            new_state = self.get_next_state()
            print(new_state[0])
            self.board.set_car_coordinates()

            # nodes = self.any_moves_pruned(new_state)

            if not self.board.is_solved():
                self.build_children(new_state)
                print("\n\n")
            else:
                self.check_solution(new_state)
                print("Game is solved")


        print(f"{self.states[0].grid}")


    def run2(self):

        i = 1
        while self.states:
        # for j in range(7):
            new_state = self.get_next_state()
            new_move = self.get_next_move()
            self.board.grid = copy.deepcopy(new_state[0])
            self.board.set_car_coordinates()

            self.board.move_car(new_move[0], new_move[1])
            # self.memory = list(zip(*self.states))[0]

            if not any(np.array_equal(self.board.grid, state[0]) for state in self.states):
                self.moves.append(new_move)
                self.states.append([copy.deepcopy(self.board.grid), new_move])
                self.node += 1

                self.board.generate_moveability()
                self.stack_moves()

            if self.board.is_solved():
                print(f"Solution {i}")
                i += 1
                break
            else:
                print(f"{self.board.grid}")
                print("\n\n")
                print(f"{self.moves}")
                print("\n\n")
                print(f"{self.states}")
                print("\n\n")


            # if not self.board.is_solved():
            #     self.build_children(new_state)
            #     print("\n\n")
            # else:
            #     self.check_solution(new_state)
            #     print(f"Game is solved with in total {len(self.check_solution())} steps")


    def stack_moves(self):
            for car in self.board.get_moveable_cars():
                for direction in car.get_legal_moves():
                    new_move = [car, direction, self.node]
                    self.moves.append(new_move)
