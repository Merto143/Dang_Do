from codefiles.algorithms.depth_first import DepthFirst

class DepthFirst_break(DepthFirst):

    def run(self):
        k = 1
        i = 1
        while self.stack:
            item = self.stack.pop()
            current_state = item[0]
            current_move = item[1]
            current_state.generate_moveability()
            print(f"Iteration {i}")
            self.node += 1

            if not (len(self.solution) != 0 and self.nr_moves >= len(self.solution)):
                self.visited.append([copy.deepcopy(current_state.grid), current_move])
                i += 1

                if not current_state.is_solved():
                    self.moves = self.create_moves(current_state)
                    for move in self.moves:
                        current_state.move_car(move[0], move[1])
                        current_state.set_car_coordinates()
                        self.history = list(zip(*self.visited))[0]
                        if not any(np.array_equal(current_state.grid, state) for state in self.history):
                            self.stack.append([copy.deepcopy(current_state), move])
                        current_state.undo_move(move[0], move[1])
                    print()

            if current_state.is_solved():
                print(f"We have found solution nr {k}!")
                k += 1
                for move in self.find_solution():
                    print(move)
                print(f"Total moves of: {len(self.solution)}")
                if len(self.solution) <= self.best_solution or self.best_solution == 0:
                    self.best_solution = len(self.solution)
                print(f"Our best solution so far: {self.best_solution}")
                print("\n\n")


        print("We have visited all possible states with depth first")
        print(f"best solution is: {self.best_solution}")
