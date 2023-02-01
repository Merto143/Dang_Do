import copy
import numpy as np

from codefiles.algorithms.depth_first import DepthFirst

class DepthFirst_depth(DepthFirst):

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
            current_depth = self.get_depth(item)
            self.increase_node()
            self.add_to_visited(current_state, current_move, current_depth)

            if self.best_solution == 0 or current_depth < self.best_solution:
                i += 1

                if not current_state.is_solved():
                    self.moves = self.create_moves(current_state)
                    for move in self.moves:
                        current_state.move_car(move[0], move[1])
                        current_state.set_car_coordinates()
                        shallow = True
                        for state in self.visited:
                            if np.array_equal(current_state.grid, state[0].grid):
                                old_depth = state[2]
                                if old_depth <= current_depth:
                                    shallow = False
                                    break
                        if not any(np.array_equal(current_state.grid, state[0].grid) for state in self.visited) or shallow:
                            self.add_to_stack(current_state, move, current_depth + 1)
                        current_state.undo_move(move[0], move[1])
                    print()
                else:
                    print(f"We have found solution nr {k}!")
                    k += 1
                    self.display_solution()
                    print(f"Total moves of: {len(self.solution)}")
                    new_sol = len(self.solution)
                    if new_sol <= self.best_solution or self.best_solution == 0:
                        self.best_solution = new_sol
                    print(f"Our best solution so far: {self.best_solution}")
                    print("\n\n")
                    # break


        print("We have visited all possible states with depth first")
        print(f"best solution is: {self.best_solution}")
