import copy
import numpy as np

from codefiles.algorithms.depth_first import DepthFirst

class DF_clear(DepthFirst):

    def run(self):
        branch_done = False
        i = 1

        while self.stack:
            print(f"Iteration {i}")
            if branch_done:
                item = self.stack.pop(0)
            else:
                item = self.pop_next_item()
            self.board.grid = copy.deepcopy(self.visited[item[2]][0])
            self.board.set_car_coordinates()
            self.board.move_car(item[0], item[1])
            self.depth = self.get_depth(item)

            self.seen_grids = list(zip(*self.visited))[0]
            if not any(np.array_equal(self.board.grid, grid) for grid in self.seen_grids):
                self.moves.append(item)
                self.visited.append([self.board.grid, item])
                self.increase_node()

                self.board.generate_moveability()
                self.create_next_moves()

            if self.board.is_solved():
                self.display_solution()
                self.compare_solutions()
                next = self.stack[0]
                if next[-1] == 1:
                    self.stack.append(next)
                    self.visited = [[copy.deepcopy(self.start.grid), "-", 0]]
                    # self.seen_grids = []
                    self.board = self.start
                    self.board.generate_moveability()
                    self.create_next_moves()
                    branch_done = True
                else:
                    branch_done = False
            else:
                branch_done = False

            i += 1


        print(f"Our best solution is {self.best_solution}")

    def find_solution(self):
        self.solution = []

        self.solution.insert(0, self.visited[-1][1])
        print(self.visited[-1])
        current_node = self.visited[-1][1][2]

        while current_node != 0:
            self.solution.insert(0, self.visited[current_node][1])
            new_node = self.visited[current_node][1][2]
            current_node = new_node

        return self.solution
