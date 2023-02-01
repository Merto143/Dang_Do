from codefiles.algorithms.algorithms import random_only_legal_moves_memory_algorithm
from codefiles.algorithms.breadth_first import *
from codefiles.classes.board import Board


class BreadthFirstRandomStates(BreadthFirst):
    def __init__(self, game, random_repeats):
            super().__init__(game)
            self.reps = random_repeats
            self.run_random()

            self.game = Board(self.game.dim, self.game.filename)

            self.game.generate_moveability()
            self.cars = self.game.get_moveable_cars()
            self.enque_movable_cars()

    def run(self):
        while not self.game.is_solved():
            self.move = self.queue.dequeue()
            self.game.id = self.grid_memory[self.move[2]][0]
            self.game.get_board_with_id()

            self.game.move_car(self.move[0], self.move[1])

            if self.game.is_solved():
                self.add_state_to_memory()
                self.node += 1

            if self.state_not_in_memory() and self.state_in_random_memory():
                self.add_state_to_memory()
                self.node += 1

                self.create_children()
                self.enque_movable_cars()

        self.print_solution()


    def run_random(self):
        self.random_memory = random_only_legal_moves_memory_algorithm(self.game, self.reps)

    def state_in_random_memory(self):
        id = self.game.get_id()
        if id in self.random_memory:
            return True

        return False
