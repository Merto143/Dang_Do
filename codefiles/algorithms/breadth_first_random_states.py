from codefiles.algorithms.algorithms import random_only_legal_moves_algorithm_with_memory
from codefiles.algorithms.breadth_first import *
from codefiles.classes.board import Board


class BreadthFirstRandomStates(BreadthFirst):

    def run(self):
        self.run_random()

        self.game = Board(self.game.dim, self.game.filename)

        while not self.game.is_solved():
            self.move = self.queue.dequeue()
            self.game.grid = copy.deepcopy(self.grid_memory[self.move[2]][0])
            self.game.set_car_coordinates()

            self.game.move_car(self.move[0], self.move[1])

            if self.state_not_in_memory() and self.state_in_random_memory():
                self.add_state_to_memory()
                self.node += 1

                self.create_children()
                self.enque_movable_cars()

        self.print_solution()


    def run_random(self):
        self.random_memory = random_only_legal_moves_algorithm_with_memory(self.game)

    def state_in_random_memory(self):
        if any(np.array_equal(self.game.grid, item) for item in self.random_memory):
            return True

        return False
