import copy
import numpy as np

class DepthFirst:
    def __init__(self, game):
        self.board = copy.deepcopy(game)
        self.board.generate_moveability()

        self.states = [copy.deepcopy(self.board)]

        # self.grid_memory = []
        self.move_memory = []

        self.best_solution = None


    def get_next_state(self):
        return self.states.pop()


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


    def check_solution(self, game):
        print("We have a solution")


    def run(self):
        print(f"{self.states[0].grid}")

        while self.states:
            new_state = self.get_next_state()

            # nodes = self.any_moves_pruned(new_state)

            if not new_state.is_solved():
                self.build_children(new_state)
            else:
                self.check_solution(new_state)
                print("Game is solved")
