import copy
import numpy as np

from codefiles.algorithms.depth_first import DepthFirst

class DepthFirst_break(DepthFirst):

    def run(self):
        i = 1
        while self.stack:
            item = self.go_to_next_state()
            print(f"Iteration {i}")
            current_state = self.get_state(item)
            current_move = self.get_move(item)
            self.increase_node()

            if not (len(self.solution) != 0 and self.nr_moves >= len(self.solution)):
                self.add_to_visited(current_state, current_move)
                i += 1

                if not current_state.is_solved():
                    self.moves = self.create_moves(current_state)
                    for move in self.moves:
                        current_state.move_car(move[0], move[1])
                        current_state.set_car_coordinates()
                        self.history = list(zip(*self.visited))[0]
                        if not any(np.array_equal(current_state.grid, state) for state in self.history):
                            self.add_to_stack(current_state, move)
                        current_state.undo_move(move[0], move[1])
                    print()

            if current_state.is_solved():
                print(f"We have found a solution!")
                for move in self.find_solution():
                    print(move)
                print(f"Total moves of: {len(self.solution)}")
                break
